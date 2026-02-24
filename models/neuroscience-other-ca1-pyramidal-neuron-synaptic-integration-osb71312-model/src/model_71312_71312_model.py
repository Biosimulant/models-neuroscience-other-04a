# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Auto-generated BioModule wrapper for 71312.

Source: opensourcebrain:71312
Original: https://github.com/OpenSourceBrain/71312
Standard: other

"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Set, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing only
    from biosim import BioWorld

import biosim
from biosim.signals import BioSignal, SignalMetadata

class Other71312(biosim.BioModule):
    """BioModule wrapper for: 71312.""""""

    def __init__(self, model_path: str = "data/repo", min_dt: float = 0.01) -> None:
        self.min_dt = min_dt
        self._model_path = Path(__file__).parent.parent / model_path
        self._t = 0.0
        self._outputs: Dict[str, BioSignal] = {}
        self._extracted_dir: Optional[Path] = None
        self._sim_format: str = "unknown"
        self._sim_files: Dict[str, list] = {}

    def setup(self, config: Optional[Dict[str, Any]] = None) -> None:
        self._t = 0.0
        self._extracted_dir: Optional[Path] = None
        self._sim_format: str = "unknown"
        self._sim_files: Dict[str, list] = {}

        data_dir = self._model_path
        if data_dir.suffix == ".zip" and data_dir.is_file():
            import zipfile
            extract_to = data_dir.parent / data_dir.stem
            if not extract_to.exists():
                with zipfile.ZipFile(data_dir, "r") as zf:
                    zf.extractall(extract_to)
            data_dir = extract_to
        self._extracted_dir = data_dir

        if data_dir.is_dir():
            all_files = [f.name for f in data_dir.rglob("*") if f.is_file()]
            exts: Dict[str, list] = {}
            for name in all_files:
                ext = Path(name).suffix.lower()
                exts.setdefault(ext, []).append(name)
            self._sim_files = exts

            if ".mod" in exts or ".hoc" in exts:
                self._sim_format = "neuron"
            elif ".nml" in exts or (".xml" in exts and any("neuroml" in n.lower() for n in exts.get(".xml", []))):
                self._sim_format = "neuroml"
            elif ".cellml" in exts:
                self._sim_format = "cellml"
            elif ".sbml" in exts or (".xml" in exts and any("sbml" in n.lower() for n in exts.get(".xml", []))):
                self._sim_format = "sbml"
            elif ".py" in exts:
                self._sim_format = "python"
            elif ".m" in exts:
                self._sim_format = "matlab"
            elif ".r" in exts or ".R" in exts:
                self._sim_format = "r"
            elif ".ipynb" in exts:
                self._sim_format = "notebook"
            elif ".cpp" in exts or ".c" in exts:
                self._sim_format = "c_cpp"
            elif ".java" in exts:
                self._sim_format = "java"

    def reset(self) -> None:
        self._t = 0.0
        self._outputs = {}

    def inputs(self) -> Set[str]:
        return set()

    def outputs(self) -> Set[str]:
        return {"state"}

    def advance_to(self, t: float) -> None:
        """Advance simulation — dispatches to detected simulator."""
        if self._extracted_dir is None:
            self.setup()

        self._t = t
        source_name = getattr(self, "_world_name", self.__class__.__name__)
        state_data: Dict[str, Any] = {"t": t, "format": self._sim_format}

        if self._sim_format == "neuron":
            mod_files = self._sim_files.get(".mod", [])
            hoc_files = self._sim_files.get(".hoc", [])
            state_data["mod_files"] = len(mod_files)
            state_data["hoc_files"] = len(hoc_files)
            try:
                from neuron import h
                state_data["neuron_available"] = True
            except ImportError:
                state_data["neuron_available"] = False

        elif self._sim_format == "neuroml":
            nml_files = self._sim_files.get(".nml", [])
            state_data["nml_files"] = len(nml_files)
            try:
                from pyneuroml import pynml
                state_data["pyneuroml_available"] = True
            except ImportError:
                state_data["pyneuroml_available"] = False

        elif self._sim_format == "sbml":
            xml_files = self._sim_files.get(".xml", []) + self._sim_files.get(".sbml", [])
            state_data["sbml_files"] = len(xml_files)
            try:
                import tellurium
                state_data["tellurium_available"] = True
            except ImportError:
                state_data["tellurium_available"] = False

        elif self._sim_format == "python":
            py_files = self._sim_files.get(".py", [])
            state_data["py_files"] = len(py_files)
            state_data["py_names"] = py_files[:10]

        elif self._sim_format == "matlab":
            m_files = self._sim_files.get(".m", [])
            state_data["m_files"] = len(m_files)
            state_data["m_names"] = m_files[:10]

        else:
            # Report what files we found
            state_data["file_types"] = {
                ext: len(files) for ext, files in self._sim_files.items()
            }

        self._outputs = {
            "state": BioSignal(
                source=source_name,
                name="state",
                value=state_data,
                time=t,
                metadata=SignalMetadata(
                    description=f"{self._sim_format} model state",
                    kind="state",
                ),
            )
        }

    def visualize(self) -> Optional[Dict[str, Any]]:
        """Visualize model structure and detected format."""
        state = self._outputs.get("state")
        value = state.value if state and isinstance(getattr(state, "value", None), dict) else {}
        fmt = value.get("format", "unknown")

        lines = [f"Model Format: {fmt}", f"Time: {self._t}s"]
        if fmt == "neuron":
            lines.append(f"MOD files: {value.get('mod_files', 0)}")
            lines.append(f"HOC files: {value.get('hoc_files', 0)}")
        elif fmt == "neuroml":
            lines.append(f"NML files: {value.get('nml_files', 0)}")
        elif fmt == "python":
            lines.append(f"Python files: {value.get('py_files', 0)}")
        elif fmt == "matlab":
            lines.append(f"MATLAB files: {value.get('m_files', 0)}")
        else:
            for ext, count in value.get("file_types", {}).items():
                lines.append(f"{ext}: {count} files")

        return {
            "render": "text",
            "data": {"text": "\n".join(lines)},
            "description": f"{fmt} model",
        }

    def get_outputs(self) -> Dict[str, BioSignal]:
        return dict(self._outputs)

# Canonical alias for stable entrypoint naming.
Model7131271312Model = Other71312
