# Mirror Generator
## How does it works ?
1. Clone this repository.
2. Create a github developper token with all permissions (I don't know which one you must take) and authorize Epitech.
3. Change `[your token]` of `data.json` file by ... your token (NO WAY?!?). So, it should looks like this:

    ```json
    {
    "token": "itsnotatokenbutyoumayunderstand"
    }
    ```
4. Download [Python](https://www.python.org/) (Don't you already have it?). Then    download [Pip](https://pypi.org/project/pip/) and, with it, download [PyGithub](https://github.com/PyGithub/PyGithub).
5. Now, you can simply use it like this:
    ```so-you-are-a-man-of-culture-as-well
    ./main.py [an ssh link]
    ```
    Where `[an ssh link]` must be replaced by an ssh link of an Epitech project. So, it should looks like this:
    ```may-be-the-best-project-ever
    ./main.py git@github.com:EpitechPromo20XX/B-DOP-200-NAN-2-1-chocolatine-your.name.git
    ```

### And that's all! You can now create mirrors of any Epitech project with a little (and free :wink:) CI/CD workflow.

## Flags:
You can add put some flag to affect the program.
Exemple:
```griffith-better-than-guts
./main.py [an ssh link] -m mirror_name --friend lhay9 -f Queng123
```
This command line will create the mirror with `mirror_name` name and add [`lhay`](https://github.com/lhay9) and [`Queng123`](https://github.com/Queng123) user to mirror repository.

There is the exhaustive list of available flags:
| Flag                                      | Description                            |
|-------------------------------------------|----------------------------------------|
| -h, --help                                | Show help message and exit             |
| --friend FRIEND, -f FRIEND                | Can add friend to mirror repository.   |
| --mirror-name MIRROR_NAME, -m MIRROR_NAME | Change the mirror repository name.     |
| --commit FIRST_COMMIT, -o FIRST_COMMIT    | Change the first commit on repository. |
