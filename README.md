Preview images inside sublime text 3 (and possibly 2)
=====================================================

Uses ImageMagick for scaling and format conversion. 

```
                ,,;<<<<<<<<<"";:"',_,,,,,,,,,,,,,,,,,,,,,  ,,vywaaaaaaawz+++aaaawaqqQqQQmqQQQQqmYHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
           _,,<<<<<<<<<""'  _"jyyyv:_yy/yyc yycjyy_yyyyycv3'yy/yyc'yyyyv=z+3'yyyc9'yy:jyc'yyyyv=4HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
       ,,;<<<<<<<<=""       :_&W T4C:WWcWWL WWLjW& ^9W&?-z9 WWLWWL WWF9WLj?djW&WWj WWkjWL WWF9WQjHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
  _,,<<<<<<<<=""            :_!WWyv::WWQWWL WWLjW&jLjW&=!59 WWLWWL WW6JWL3aLjWLWW, WWWWWL WWLjWWjHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
;<<<<<<<=""                 : yy=WWL;WWCWWL WWLjW&jLjW&=<,] WWLWWL WWF,vyB4'WW6WWL WW9WWL WWLjWWjHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
<<<=""                      : 9WyWW^=WWcWWL !W6QWCjLjWW:<<<_9WqWW^_WWLjYJHJ,WWL9WQ WW WWL WW6WWPjHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
"                          _,,yv,,yJv,,yvvyJ\_  _356yyvc<<<>,_,_,/_jvyJHHHHyvvyyvvyvvyyvyyvvvvyyBHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                      _,vvz7?+++?L:)a++i2^;,<<<<<<,,<=!L=<<<<<-=<<</BHHHHHHHHHGHHHHHHGHHHJHHHHHaHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                 ,,vv+?t+++++++++i=;;?w^,<<<<<<<<<<<<<<;;<<<<<<<<<<<]WHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
           _,,vv7?t++++++++++????!:<<;,<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-9HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
      _,vvz7?++++++++++++++iav"<<<<<<<<<<<<<="""""<<<<<<<<<<<<<<<<<<;j3HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
 ,,vv+?t++++++++++++++iaaHHHHH6v=<<<<<<<<<<;/9HHaavvv/="=<<<<<<<<<<</jJHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
7?t++++++++++++++aaaHHHHHHHHHHHON-<<<<<<<<==<;=HHGaHHOHGvv,=""<<<<<=>BHHHHHHHHHHHHHHHO)<<????(\vv><??!HHHHHHHHHHHHHHHHHHHHHHHHHH
++++++++++++aaJHHHHHHHHHHHHHHHHH'<<<<<<<<,)yvv=jHHHHHHHHaHOYHacyyvywBHHHHHHHHHHHHH^^>==^= ,,,,,,_j"') t==7YYHHHHHHHHHHHHHHHHHHHH
++++++iaaHHHHHHHHHHHHHHHHHHHHHHL;<<<<<<<<<;/YYHHHHHHHHHHHHHHHG6v)HHHHHHHHHHHHHHHHHr' <         c )__  ' ;;7?HHHHHHHHHHHHHHHHHHHH
+aaaHHHHHHHHHHHHHHHHHHHHHHHHHH9-<<<<<<<<<<<</YHHHH???????Hr??)+7C4HHHHHHHHHHHHHHHW!-y'         :j _' "p' =:"=WHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHL=<<<<<<<<<<<</HHH\yWWWWmyy=yWWWX4x9HHHHHHHHHHHHHP=  "c         _r_- _7  y_  =)9HHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH4x"<<<<=\yvy;=-3YGjWWWk jWWQjWWWqyW;HHHHHHHHHHHQP/    =c        j'/ _^ ,='  _ ""4HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHmv"==jY/v/Hc"j3H]WWWWWWWWFJ!4WWWtJHHHHHHHHHH?=]'_    j        r: _',^   ,>c,,<>HHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHByv)Hb79YJuJJH67!TNNT!5JH5v??;79HHHHHHHHHvv\,, ;    L       ''_;/'_,>vvwaHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH6/???(JHHHHHHGaavwaHHHGHHHHGrjHHHHHHHHHHHH44Gav,_=      :__;^,>c7HHHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHGwjJHHHHHHHHHHHHHHHGvv<<<=yHHHHHHHHHHHHHHHHHd?vwO?Hav_ -/=)jO?63HHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHOjYHH?HHHHHHHHHHHHHHHHHH57QHHHHHHHHHHHHHHHPjOHaHGa+??GvjwJY?GPjHHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHYHqqLJHHH75yyyyp(???YHHHHHHHHG/!HHHHHHHHHHHHH4;GHHHY(????9\JaJO?(/4HHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH????md!^" jGHH'   :!!!!!9d+(????HHHGHbjHHHHHHHHH?HHQ]GHHH3/'   ,vvvvvwHC3JHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHOYHmqQH?!!!!^    _OHHG,"'_,     w_maJaavvvvvvvHHHHHHOHqd!!^^:GHHH3=   ]HHHHHO?(v]HHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHH?HqQ!!!^'            JHHHHOHavvvvvvvOu]HHHHHHHHHHHHHHHYqf!'     :eHHHJ'     v/vvvwH7jHHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHH?Hqd!!'                 )GHHHHHHGaaaaad?!!jHYHHHHHHHHHHYmd!'         )GOtP/v    ??????']WHHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHYmW!!'                    j6/?HHHHHHHHHGP'    7!QqqHHHHHqd!^             :??, )_,_     _:j:]HHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHOYqd!^                       jWWWyp7???????(          ==!!!^'                   ^j  :^^^"""',) 'YHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHYqd!'                          WWWWWWWWmqqqQW'                                      v<,,,;"<<<vvvw???HHHHHHHHHHHHHHHHHHHHH
HHHYmd!'                            =!!!!!!!!!!WWX!                                        /!!!!!!!!!!!!!!!HHHHHHHHHHHHHHHHHHHHH
OmW!'                ;WWWWWL WWWW  WWkjQW QQQQLjWLQWW6jWWWc4WLjWX   QWWQjWWWL,yW&WqcjWWcjWL_WQQWcWWcjQPjQWcmHHHHHHHHHHHHHHHHHHHH
!^                     3WW  jWWWWL WWWWW^cWW&  WWL4WWWJWWWL=WQWW^   9WWWJWWWLjWW WWLjWWQJWL:WWL _]WQWW'jWW-&HHHHHHHHHHHHHHHHHHHH
                       3WW -jWFjWk WWWWW=LWWWTLQWL4WWWWWWWL_9WWF    9WWWWWWWLjWW WWLjWWWWWL:WW&4 c9WWLj=WW EHHHHHHHHHHHHHHHHHHHH
                       3WW  WWWWWW WWX4Wk WWQ_/9WL4WFWWFWWCyjWW-    9WF4WFWWLjWW WWL]WW9WWL:WWL_/bjWW W X4 EHHHHHHHHHHHHHHHHHHHH
                 vy'   3!4  T!L]!!'!!C]!!-!!!!CjW'!!L94'!!'&=!!'#wyc!!L]!'!!^c!!T!!j=!! !!C:!!!!C+]!! &=!!'EHHHHHHHHHHHHHHHHHHHH

```


Installation
------------

Make sure you have ImageMagick installed.

To install this plugin manually go to the "Packages" directory `Preferences -> Browse Packages...` Then clone this repository:

```
git clone git://github.com/possan/sublime_image_preview
```


Usage
-----

Click on a PNG, GIF or JPEG file, and you will see an ascii preview of it inside your favorite text editor.

