import click
import os


def log(icon: str, message: str):
    print(f"\n{icon}: {message}\n")


def create_new_day_folder(folder: str):
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.system("cp -r days/template/* " + folder)
        log("✅", "Folder created properly.")
    else:
        log("❌", "Folder already created. Remove it before creating a new one.")


@click.command()
@click.option(
    "-d", "--day", prompt="Day", type=click.IntRange(1, 24), help="Day you want to run"
)
@click.option(
    "-t", "--test", is_flag=True, default=False, help="Run the tests for this day"
)
@click.option(
    "-c",
    "--create",
    is_flag=True,
    default=False,
    help="Create new folder for a new day",
)
def cli(day, test, create):
    folder = f"days/day_{day}/"

    if create:
        create_new_day_folder(folder)
        return

    if not os.path.exists(folder):
        log("❌", "The day doesn't exist yet. Please create it with -c flag.")
        return

    if test:
        os.system(f"PYTHONPATH={folder} pytest {folder}")
        return

    os.system(f"PYTHONPATH={folder} python {folder}main.py")


if __name__ == "__main__":
    cli()
