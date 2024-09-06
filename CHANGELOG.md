# CHANGELOG

## v2.1.0 (2024-09-06)

### Feature

* feat(db): add a db model for a track like ([`0cafb39`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/0cafb392fb9b54f35ee59701063ae112d3f744ee))

* feat(db): add a db model for a playlist ([`8e965be`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/8e965bef5ba3f29e3a58ecabb1278059ba7f741e))

* feat(db): add a db model for a track ([`0946d3b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/0946d3b4d72b11fc6522d04e006bfbcffdbd2024))

* feat(social): add a db model for a person ([`6fce200`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/6fce200459ba449185e0d504b81a8832b7c020eb))

* feat(music): create a package for music models ([`70f9b5e`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/70f9b5e5ccfc9cc5ac6550c38bb33be598fed766))

* feat: add media settings ([`eaea217`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/eaea21738912ee3477e09276c4b07447e1375333))

### Refactor

* refactor(db): remove WithOwnerMixin class ([`7a2ba27`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/7a2ba27e9cc1e47fe825fcbdb5b75502544e5484))

### Style

* style: run &#34;make format&#34; ([`caeedfe`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/caeedfe4775d5ad3508ec39d67f98ec5397ef424))

## v2.0.0 (2024-09-03)

### Breaking

* feat(users)!: add custom user model

BREAKING CHANGE: drop all under &#34;auth&#34; before updating to this ([`92543e5`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/92543e5fca725ed53c1b552ccdacb93351ebe059))

### Chore

* chore: add python-semantic-release configuration ([`afd3a88`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/afd3a8852e3c25726ff933dae869c2492b3a956b))

* chore(deps): install python-semantic-release ([`a384775`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/a384775998c7bfa8c5be4d5dcc4ecff00f4f473c))

* chore: add configuration files for linters ([`19b928c`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/19b928ccfa673e460bc32e4e983d9272804fcc35))

* chore(make): add &#34;make-migrations&#34; and &#34;migrate&#34; goals ([`615a9f1`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/615a9f137eed5a959826e688068c2fe3eccd817f))

* chore(deps): install django-filter ([`80b214d`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/80b214de9b0b41be8d9397c3ddcbf3d31f26ee79))

* chore(deps): install django-split-settings ([`a53d6af`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/a53d6afffed971ecf806f13103b19cb93964227a))

* chore(deps): freeze requirements ([`b4baa5f`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b4baa5fdd0fb45782c326fc2bc5203a827f2ae3d))

* chore(make): add Makefile ([`56dd238`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/56dd2387aaea4a734cd63e2dc67f51a6972f514d))

* chore(deps): add files with project dependencies ([`3be0133`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/3be0133b766f6f6998867035eed47a51d1d79ccb))

* chore: add README ([`8228fd1`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/8228fd1bd1e90397b85833bc53c09f5780298c57))

* chore: add LICENSE ([`aa84dad`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/aa84dad63de1376ed7ab9cde3a1a63ba1bf41e53))

* chore(git): add gitignore ([`5d63075`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/5d6307592ea736ee1d383436ff9076c4dce4efb8))

### Ci

* ci: add pre-commit config file ([`1433713`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/143371368783235385ee2e7a519a7eb4d471696f))

### Documentation

* docs(env): add a template file with environment variables ([`b806102`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b806102044b88d0fc9fa486fc08c7d7a82130574))

### Feature

* feat(auth): add API for authentication ([`4251c59`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/4251c596d7f6aa0c26bfd59191ace6cfa07afcfc))

* feat(api): add common api tools ([`e5b6b9b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/e5b6b9bdcf07e618d1988fa58d47eb053aa2e939))

* feat: add common models ([`2594812`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/2594812f8a26ba208aa2b2b827ad05756413c61e))

* feat(core): add common exception handler ([`ee8ddd9`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/ee8ddd98733128b41eb76218542cede00cb63dcd))

* feat(config): include all settings files in the main one ([`f00e6ad`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/f00e6adad646a5db25d3ccfc0faa59503ff7484d))

* feat(config): add a settings file for the templates ([`701b0ef`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/701b0ef8bf210d8262af558853a60136b4882647))

* feat(config): add a settings file for static files ([`40052f9`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/40052f96549c6fdeeda5d08f5d7901834e32a078))

* feat(config): add a settings file for rest_framework ([`cc8479d`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/cc8479d8b12051fe70f1d90e7dbf6473b3e41f3a))

* feat(config): add a settings file for drf-spectacular ([`eb8d9b8`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/eb8d9b803111f252d898a88e7775ec953ad9ad2e))

* feat(config): add a settings file for the middleware ([`6d70e03`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/6d70e03a258b12ff33c64a00b8c3fbeb046a0aa8))

* feat(config): add a settings file for installed applications ([`ea3b3bf`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/ea3b3bfe69b5894b1945eb8a473f6cf0597b0a42))

* feat(config): add a settings file for djoser ([`e5f9348`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/e5f9348655d465bfbd2fb738bc804434f4003a21))

* feat(config): add a settings file for debug mode ([`1d2f1fd`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/1d2f1fd3242638a8519f3e372aacf687c173a650))

* feat(config): add a settings file for the database ([`daa348b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/daa348b89054abc17633eb3d9ae669094f02342f))

* feat(config): add a settings file for the django-cors-headers application ([`9f5bfe1`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/9f5bfe100348d00911f5e7bf06673e62b190ca8a))

* feat(config): add a settings file for the application name and description ([`f9efea4`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/f9efea4e2207ae62ec89110cd38aae4d7661b8b7))

* feat(config): added a tool for reading environment variables from a file ([`1918ddd`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/1918dddcbf07e0af7c4124389703381934701c50))

* feat: add package for settings modules ([`f699252`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/f6992522a845086505eb71be6f7dacac9dfb55b1))

### Refactor

* refactor(config): move the main project settings to a separate file ([`93bd7cb`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/93bd7cb3d0fd127d242fa9dc4e2c64fb46d933b0))

### Style

* style: run &#34;make format&#34; ([`1b90489`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/1b90489e815f6425fc0b5411d105a64043c54af5))
