from typing import Optional

import typer
import requests

from dictionary import __app_name__, __version__, __api_key__

app = typer.Typer(add_completion=False)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
        version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
    )
) -> None:
    return

@app.command()
def word(word: str):

    if word.isnumeric():
        typer.echo("Please enter a valid word, integers are not allowed.")
        exit(1)

    url = "https://dictionaryapi.com/api/v3/references/learners/json/"
    url = url +word+"?key="+f"{__api_key__}"



    response = requests.request("GET", url, headers={}, data={})
    if response.status_code != 200:
        typer.echo(response)
        exit(1)
    res = response.json()


    if type(res) == list and len(res) ==0:
        typer.echo("Please provide a valid word.")
        exit(1)
    if type(res[0]) != dict:
        typer.echo("Please provide a valid word.")
        exit(1)

    try:

        if "prs" in res[0]["hwi"]:
            prunciation = res[0]["hwi"]["prs"][0]["ipa"][1:]
        else:
            prunciation = res[0]["vrs"][0]["prs"][0]["ipa"][1:]
    except:
        prunciation = word


    speech = res[0]["meta"]["app-shortdef"]["fl"]
    definition = res[0]["meta"]["app-shortdef"]["def"][0]
    curly_index = definition.rfind('}')
    definition = definition[curly_index +1:]

    result = "`"+prunciation + "` (" +speech +"): " + definition
    typer.echo(f"{result}")
    #print(res[0]['meta']['id'])

