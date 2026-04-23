# ForgeDRM - The first-ever open source DRM

Everything is stored locally, meaning it is hard to globally attack your app if it's ever hacked into,

No server needed, it all stores into a UUID! Here is a example of how to use it:

```python
import forgedrm

license_id = packageWithID("myGame", "packagedGame.zip")
print(f"Store this server-side: {license_id}")
```

`myGame` isn't required but is useful for game names, same for `packagedGame.zip`

printing is just apart of example and not needed either.

A hard to read folder structure and a UUID zip password makes it extra-hard to hack into because it will be (nearly) impossible to look for the game files!

## Required dependencies

`pip install pyzipper`
