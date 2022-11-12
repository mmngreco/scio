# issue

```bash
~  (10:41|32s)
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't
have a Docker ID, head over to https://hub.docker.com to create one.
Username: mmngreco
Password:
Error saving credentials: error storing credentials - err: exit status 1, out:
`exit status 1: gpg: 1616D81854845176: There is no assurance this key belongs
to the named user
gpg: [stdin]: encryption failed: Unusable public key
Password encryption aborted.`
~  (10:41|16s)

```

After some research I found out [this
post](https://nono.ma/there-is-no-assurance-this-key-belongs-to-the-named-user-gnupg-trust)
and this [SO
entry](https://stackoverflow.com/questions/33361068/gnupg-there-is-no-assurance-this-key-belongs-to-the-named-user)

## solution

```bash
$ gpg --list-keys
$ gpg --edit-key <key-uuid>
$ gpg > trust
$ gpg > 5
$ gpg > quit
$ docker login  # it should work
```



