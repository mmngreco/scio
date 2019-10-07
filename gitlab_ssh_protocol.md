# SSH git clone url format on gitlab

General syntax:

```
<protocol>://[<user>[:<password>]@]<hostname>[:<port>][:][/]<path>[#<commit-ish> | #semver:<semver>]
                                    prefer the slash here ^
```

These URLs work:

```
# with slash between host & path
git+ssh://git@gitlab.example.com/path/repo.git
git+ssh://git@gitlab.example.com/path/repo.git#branch_1_2
git+ssh://git@gitlab.example.com/path/repo.git#1.2.3
git+ssh://git@gitlab.example.com/path/repo.git#semver:^1.2.3
git+ssh://git@gitlab.example.com/path/repo.git#semver:~1.2.3

# with colon between host & path
git+ssh://git@gitlab.example.com:path/repo.git
git+ssh://git@gitlab.example.com:path/repo.git#branch_1_2
git+ssh://git@gitlab.example.com:path/repo.git#1.2.3
```

These don't work:

```
# with colon between host & path
git+ssh://git@gitlab.example.com:path/repo.git#semver:^1.2.3
git+ssh://git@gitlab.example.com:path/repo.git#semver:~1.2.3
```

Be aware with the remote url after `git clone git+ssh:URL` because your origin
url is `git+ssh:URL` which could not be what you want.

```
git remote get-url origin  # ->> git+ssh:URL
git remote set-url origin URL
```

## Source:

* https://gitlab.com/gitlab-org/gitlab-ce/issues/46053
* https://gitlab.com/gitlab-com/support-forum/issues/1665
* https://help.github.com/en/articles/which-remote-url-should-i-use#cloning-with-https-urls-recommended
* https://help.github.com/en/articles/about-authentication-with-saml-single-sign-on
