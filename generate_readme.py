"""
ルートの目次自動作成用
"""
from pathlib import Path


ROOT = Path(__file__).parent
README = ROOT / "README.md"
LIST_IGNORE = [".venv", ".git"]


def create_index():

    lines = [
        "# 技術メモ",
        "今まで触った技術のメモ・備忘録用",
    ]

    for directory in sorted(ROOT.iterdir()):

        if not directory.is_dir():
            continue

        if directory.name in LIST_IGNORE:
            continue

        lines.append(
            f"## {directory.name}"
        )
        lines.append("")

        for file in sorted(
            directory.rglob("README.md")
        ):

            # ルートREADMEは除外
            if file == README:
                continue

            # README.mdの親ディレクトリ名を取得
            title = file.parent.name

            # ルートからの相対パス
            relative_path = file.relative_to(ROOT)

            lines.append(
                f"- [{title}]({relative_path.as_posix()})"
            )

        lines.append("")

    README.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )


if __name__ == "__main__":
    create_index()
