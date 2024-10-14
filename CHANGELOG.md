# CHANGELOG

## v10.0.0 (2024-10-14)

### Breaking

* feat(likes)!: install app &#34;db.likes&#34; ([`f6fd603`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/f6fd6034966eb7b1aa26a59880e030fbbec9ac39))

* feat(social)!: add target type field to the Like model

BREAKING-CHANGE: drop all under &#34;social&#34; before updating to this ([`aa9a490`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/aa9a4909ef98d9a3845eeaa27267f1ce7344aacc))

* feat(social)!: get rid of complicated model hierarchy

BREAKING-CHANGE: drop all under &#34;social&#34; before updating to this ([`c555336`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/c5553366a69ef343a5c57937940da568901025a5))

### Feature

* feat(social): add api to create and delete likes ([`ff8be9b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/ff8be9b5bc263971557b5a1a36438aa4b698da35))

* feat(social): add &#34;with_likes&#34; decorator ([`032134e`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/032134ecae8d864fbb86843af0e071ebe27eb2a7))

* feat(social): add services to create and destroy likes ([`572d6c1`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/572d6c1380ea059b3ce622df6141d834137cba2e))

* feat(social): add with_likes decorator ([`02976a8`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/02976a8005a882baede58fdf0de33b64f009b6f7))

### Refactor

* refactor(likes): move everything related to likes to a separate package ([`df1792f`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/df1792f50460e521dd929fa64cfda184087986ec))

* refactor(likes): rename &#34;api.social&#34; package to &#34;api.likes&#34; ([`c02e15f`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/c02e15f241d7047a2369df0e06c907ad1839d54f))

## v9.0.0 (2024-10-02)

### Breaking

* feat(db)!: make all models soft-deletable ([`4d0558f`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/4d0558f04f58efe1739a5e8fcf551c1928b07c1d))

* feat(social)!: add repost models to db.social.__init__ ([`e8248ec`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/e8248ec61a53fe8c08b941185a27ec87828f4487))

* feat(person)!: add intermediate model storing info about saved playlists

BREAKING-CHANGE: drop all under &#34;person&#34; before updating to this ([`dd30a72`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/dd30a72cc768bf9f8ca13f106498e8caaa965458))

### Feature

* feat(social): add &#34;parent&#34; field to CommentBase model ([`9f81c17`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/9f81c17fa46fbe923035972470dd5eb381dbbf0e))

## v8.0.0 (2024-09-27)

### Breaking

* feat(music)!: add intermediate models storing info about tracks in playlists and albums

BREAKING-CHANGE: drop all under &#34;music&#34; and before updating to this ([`95952e6`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/95952e6e45ada0ec26366f012b9435cc055d40e8))

### Feature

* feat(music): use track CRUD services in views ([`35aa755`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/35aa755bf11da39697dfcbdfbddcf15005fddb1b))

### Refactor

* refactor(music): use intermediate models in track_delete service ([`1c37042`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/1c37042befd37479d9bf6e5c80c3840186565f5d))

## v7.3.0 (2024-09-27)

### Feature

* feat(music): add CRUD services for tracks ([`082bb71`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/082bb7137946340040e061e3d879f53ef699f8db))

* feat(services): add common model_update service ([`9654543`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/965454373eaa586d9d226ec11995507b10c19503))

* feat(api): add common parsers ([`9da5c38`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/9da5c3886137f885660d570bd483c3646247e0c6))

## v7.2.0 (2024-09-24)

### Feature

* feat(music): add CRUD API stub for albums ([`3be8952`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/3be8952c94a065741b488ecc214b3e558ee18bfa))

* feat(music): add ordering fields to track and playlist views ([`8842fee`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/8842feebda994f993d45f4d86040f6fa6384989f))

* feat(music): add filterset classes for music views ([`15c6700`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/15c67004baa08c3799d81a422bc75dbc40f59f56))

* feat(api): add common filterset fields ([`dd2c76b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/dd2c76b38815838a5cbbaa7d9c247ccd0b7457ad))

* feat(api): add filter fields to api.common ([`cd1d021`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/cd1d02159750701bfcc24e44eeb9b4c55e480c9f))

### Refactor

* refactor(api): make all model serializers read only ([`aa7d91a`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/aa7d91a9e900ce78d744edee25a5db43c43b1f5b))

## v7.1.0 (2024-09-19)

### Feature

* feat(api): add CRUD API stub for playlists ([`982e0e2`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/982e0e27354070432b28c4dc9c62022eec9c8642))

* feat(music): add CRUD API stub for tracks ([`b9b946b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b9b946bcac52da1452120b3a42ce7f5b9468abea))

* feat(api): exclude PATCH requests from ModelViewSet ([`bc0497f`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/bc0497f16db97d6ff1781dfe9731c65de19edbd2))

* feat(api): add more permissions to api.common.permissions ([`90179b8`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/90179b8103e69b5679d878e24fd583dc5ac4374b))

* feat(api): add http statuses api.common ([`7a48753`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/7a48753404a03615616fdcaaab46d7a548271edf))

* feat(api): add &#34;action&#34; decorator to api.common ([`87eab39`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/87eab39dbc64fa571ae9d5264f7524b493b36aac))

* feat(api): add common responses ([`a2b9062`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/a2b9062d0d877dc50fca92ac37703fcc2b50be33))

* feat(api): add common filters ([`c69f6fa`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/c69f6fad95ff7b9661395a011327fa9de39fdb6c))

* feat(api): add common openapi utils ([`c5684d1`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/c5684d19e7197ee31edd7c31901ab2a4d5ff7018))

* feat(api): add common views ([`f1bce0e`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/f1bce0e645571a00b83af118db2de9beeb43de20))

* feat(api): add common views ([`b5b75e2`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b5b75e2e53ef498567c64a9d30262f02d9f4f8a2))

* feat(api): add common fields ([`170bdcc`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/170bdcc6b98414d1b7a2b72dda48aa1ab1854685))

* feat(api): add common schema tags ([`b3f22ca`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b3f22caf83b87863a335339a02a1ee623b0343d9))

* feat(api): add common serializers ([`1f6a17d`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/1f6a17d2a355dd756e974606e9262c6bbaa5d4d1))

* feat(music): add package for music api ([`81e5bb9`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/81e5bb92eba54024bc6f3b431cd55f1cd002684b))

* feat(api): add DataObjectSerializer ([`a207423`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/a20742343d82885d98cda0abcab1c94e83aac308))

### Refactor

* refactor(api): import &#34;fields&#34; module instead of all the field classes ([`4ef9944`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/4ef99446dda9a1c58a6c3fc57cd4f4766acfda8e))

* refactor(music): add GENRE_CHOICES to db.music.models.__init__ ([`931b2d6`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/931b2d6dd072ccfe26ad312eb68166484adcc97d))

## v7.0.0 (2024-09-16)

### Breaking

* feat(person)!: add model for person roles ([`4f721aa`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/4f721aa5896e9a7d42e6c7b855774ccbb03a8d8c))

* feat(person)!: move the Person model and WithOwnerMixin into a separate package

BREAKING-CHANGE: drop all under &#34;music&#34; and &#34;social&#34; before updating to this ([`a7a8ee6`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/a7a8ee62613bfcc6a13f174a7660795642539944))

### Refactor

* refactor(social): inherit models of comments, likes and reposts from the base SocialModel ([`bd0a404`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/bd0a40404243986f6adaea453101e76011a56ab9))

## v6.0.0 (2024-09-13)

### Breaking

* feat(social)!: add models for reposts ([`2ded5ee`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/2ded5ee89acd1e5517ce85cc186f4d054953062e))

* feat(social)!: add &#34;subscribers&#34; field to the Person model ([`233e8cf`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/233e8cfc4c85f13820fa1a2be34362fd10337686))

### Chore

* chore(make): add git push to Make&#39;s &#34;version&#34; goal ([`8402663`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/840266347d7bb85c214f7bb03a8028485c265d92))

### Feature

* feat(social): add AlbumLike model ([`967bb3b`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/967bb3b77a3dc2c46daad1c02380dcf8787b0bbd))

## v5.1.0 (2024-09-11)

### Chore

* chore(make): add &#34;version&#34; Make goal ([`36b3e46`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/36b3e46514bd5375a7cf90db35f24cf653972fbc))

### Feature

* feat: define __str__ method in models ([`ea418f0`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/ea418f029e5a0a9e06b61db4cc589ddb51a31c10))

## v5.0.0 (2024-09-10)

### Breaking

* feat(social)!: add the subject field to all comment models

BREAKING-CHANGE: drop all under &#34;music&#34; and before updating to this ([`d68e4c3`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/d68e4c3498d79996747b7ee91086588efb2adb52))

## v4.0.0 (2024-09-09)

### Breaking

* feat(social)!: use a dedicated field in all models that have an owner

BREAKING-CHANGE: drop all under &#34;music&#34; and &#34;social&#34; before updating to this ([`7f6017f`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/7f6017fd39d8f87b1d21d6be7cfe85316deb00c4))

* feat(music)!: add &#34;duration&#34; and &#34;release_date&#34; fields

BREAKING-CHANGE: drop all under &#34;music&#34; before updating to this ([`5caad19`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/5caad195b123c48246b919c6574d5f203e499db3))

### Feature

* feat(social): add &#34;WithOwnerMixin&#34; class ([`2cc0a0e`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/2cc0a0e625ce38ab5f2a9e4b08a488ee9b56ef62))

## v3.0.0 (2024-09-09)

### Breaking

* feat(social)!: make migrations

BREAKING-CHANGE: drop all under &#34;music&#34; and &#34;social&#34; before updating to this ([`b104674`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b10467484637ee1c3386a9e4b85c9d28b9cc5c80))

### Chore

* chore(make): rename &#34;make-migrations&#34; goal to &#34;migrations&#34; ([`10ec451`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/10ec451a07eb6e0f94e27dbefbeb66f3b9943750))

* chore(deps): install pillow ([`bebff30`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/bebff30c2d8d1d825c749bf06095cba82753091c))

### Feature

* feat(social): add models for likes ([`c47821d`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/c47821de34da9f8c09d623097c2a343a18fd2476))

* feat(social): add models for comments ([`98adbf0`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/98adbf0fc14eb5640b0489b36d56bff8d06cfa77))

* feat(social): add a function to create a target field in the comment and like models ([`b8cb2c0`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/b8cb2c0e2c76cd09823761302a7f55b95875ac67))

* feat(db): add a db model for a playlist like ([`75a2a57`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/75a2a57218737e72457f19fbf76c652ec8e5d9a3))

### Fix

* fix(db): fix path to the BaseModel class ([`0f28a21`](https://github.com/Ceowyllian/kubstu.music-hosting.back/commit/0f28a21705cebd8a0cfdf4395bf5ec4c53eb3ce3))

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
