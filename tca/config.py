#读取 term.yml
from pathlib import Path
from dataclasses import dataclass
import yaml

@dataclass
class Variant:
    surface: str
    is_ambiguous: bool = False

@dataclass
class Concept:
    name: str
    variants: list[Variant]

def load_concepts(path: str | Path) -> list[Concept]:
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return [
        Concept(
            name=c["name"],
            variants=[Variant(**v) for v in c["variants"]],
        )
        for c in raw["concepts"]
    ]