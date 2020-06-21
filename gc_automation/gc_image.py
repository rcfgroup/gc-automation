import io
import subprocess
import time
from sys import stdout
from typing import List, Union, Optional
from lxml import etree


class GCICmdParameter:
    """GC Image Command Parameter

    Example:
        <parameter id = "workflowType" label = "Workflow Type">TEMPLATE</parameter>
    """

    def __init__(
        self, cmd_id: str, label: str, value: Union[str, int, float] = ""
    ) -> None:
        """Create a GC Image command parameter object

        Args:
            cmd_id (str): Command parameter identifier
            label (str): Command parameter readable name
            value (str or int or float): Command parameter value
        """
        self.cmd_id = cmd_id
        self.label = label
        self.value = str(value)

    @property
    def xml_element(self) -> etree.Element:
        """Generate and return a lxml etree Element object from current instance."""
        xml_element = etree.Element("parameter", id=self.cmd_id, label=self.label)
        xml_element.text = self.value
        return xml_element


class GCIProcessChildCmd:
    """GC Image Command Parameter

    Example:
        <cmd name="methodCmdRegisterImage" label="Register Image">
            <timeStamp>8 March, 2019 16:07:17</timeStamp>
            <userName>GC Image</userName>
            <cmdversion>2.8.2</cmdversion>
            <do>
                <parameter id = "workflowType" label = "Workflow Type">TEMPLATE</parameter>
            </do>
        </cmd>
    """

    def __init__(
        self,
        name: str,
        label: str,
        timestamp: Optional[str] = None,
        username: Optional[str] = None,
        version: Optional[str] = None,
        parameters: Optional[List[GCICmdParameter]] = None,
    ) -> None:
        """Create a GC Image command parameter object

        Args:
            name (str): Command identifier
            label (str): Command readable name
            timestamp (str or None): Command creation timestamp
            username (str or None): User who creates the command
            version (str or None): Command version
            parameters (list of GCICmdParameter or None):
        """
        self.name = name
        self.label = label
        self.timestamp = timestamp
        self.username = username
        self.version = version
        self.parameters = parameters if parameters is not None else []

    @property
    def xml_element(self):
        element = etree.Element("cmd", name=self.name, label=self.label)
        if self.timestamp:
            ele_timestamp = etree.SubElement(element, "timeStamp")
            ele_timestamp.text = self.timestamp
        if self.username:
            ele_username = etree.SubElement(element, "userName")
            ele_username.text = self.username
        if self.version:
            ele_version = etree.SubElement(element, "cmdversion")
            ele_version.text = self.version
        ele_do = etree.SubElement(element, "do")
        for param in self.parameters:
            ele_do.append(param.xml_element)
        return element


class GCIProcessCmd:
    def __init__(self, configure: str, child_cmd: List[GCIProcessChildCmd] = None):
        self.configure = configure
        self.child_cmd = child_cmd if child_cmd is not None else []

    @property
    def xml_element(self):
        element = etree.Element("script")
        for cmd in self.child_cmd:
            element.append(cmd.xml_element)
        return element

    def to_cmd(self, path):
        with open(path, "w") as cmd_file:
            cmd_file.write(f"-Configure {self.configure}\n")
            cmd_file.write(
                f"-script {etree.tostring(self.xml_element, pretty_print=True).decode()}"
            )


def process_image(gci_path, method, source_path, output_path, export_path, log_path):
    with io.open(log_path, "ab") as writer, io.open(log_path, "rb", 1) as reader:
        p = subprocess.Popen(
            [
                gci_path,
                "-sysu",
                "-cmdFile",
                method,
                "-s",
                str(source_path.absolute()),
                "-d",
                output_path.joinpath(source_path.name),
                "2>&1",
                "1>nul",
                "|",
                "more",
            ],
            stdout=writer,
        )
        while p.poll() is None:
            stdout.write(reader.read())
            time.sleep(1)
        stdout.write(reader.read())
