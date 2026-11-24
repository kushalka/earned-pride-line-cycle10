"""Write one line of quiet, earned pride for the bounty's judge."""

from pathlib import Path

LINE = (
    "On her fortieth night shift the new nurse got the IV in on the first try; "
    "the old man in bed three slept through it, and she let herself smile."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
