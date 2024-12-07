import marshal, base64
def xor_encrypt_decrypt(data, key):
    return bytearray([b ^ key[i % len(key)] for i, b in enumerate(data)])
encrypted_data = base64.b85decode('4tZa5Wn*=6WnXJ$d24xJb7f<7a+cF+WqJB}J97bI8FD{g4`m%}6<#T12Xz)?Gig7233)qm31BaA0bdVf6=@?|7i9-@9$*D-0eJ~~Gj#}LFM4EO4`m&06;>W^Ie&9yJ8J=Y0dO*TKWKDv0bdVi6>Ah&DQRML7GVWu0em-iJ9a;85p+LK4`L&H9akxL2Ye`YJ7Pa=348^80ckI10b4P19cCj)7il?d7HkE00dqHOJ9j^I5qUpI4{0NH9aAZM2Ye`hJ8nN>33LT-0c|gD0Z=h@9epD~7i>9i7GMQ%0dzNIJAFTX5q&>T4|OAR9Zo5F2WKcnJ9s}>32g;Y0d_A@0ZB1I9eN{r7kxQX7JLOv0b@5&J7_;j5pF+q4|pR+9a|}A2XH8BJ8nOA34aA+0c0;@0ar119b_X+7i>9U7H<W90ev@bJ9s~I5q>{M4|gL?9ZV@i2Vp2jJAOY}32y~g0dy}{0Y@=I9dsjj7k@cj7JJ)kKUHseI&%*>b#i52Yh`(Dd0%s7V|8+6Uuywo#&}<IWn*=6WM2<O{cR(07ewcEC`vm?;dwVnJ5b?cFGB%)?`0!j9eVd=IYt&k+iO2f30~WCKUNW1;a@RR9c>+6A5u9&7G*nX33)epJ97bI8FN2g4`m%h6=xn?IZtzCJ3--jH$q)=09g@P$#cMDd2M-Lb7fX_C|NpJ4+3p@Uvp(+b#i52Yh`(Dd0%s722R;zUu$J~ZFydE0AC*oWnXJ$d2M-Lb7f<7a%Ep@WqAls^m1imb#i52YGoa49bOk?$aivOUu$J~Y<W6O0ZtxTWnUR>du<$P*kxmNa%Ep@WO)>LCUQn&L~<5h9A|iKAYXE2Vs-v<Culr*8hCbHjAM0jWf4MTqi6{&8VeU(bH7?U1Q!SuC3Jo`L`ha`1|NQQB5p`rQWywgL@-xEUQIFyVt6h<UTj$i18HIeLkJmiX+CaHTuuN3SZF>{PC-{P5n^ICNMt}!4i9yH1X^B7SQI66emF!)Tx|v)es&^mNL)}D2x3GqR6<luG6`aME<;{sUI+tfVgy27T0<WnRxn0MT}f|4RXz`UK71`BNnJ^AE+1+xQB`j(BS~E(C3-$UGc+R^TU8_%a0F0QQ#MK?88#nqHd-DvRZ}xGI3;2}S}Q+qLn9?92y6sMRY@y988tW=d?`j5Eh9fGKLQDCI94<xXDwApFauU7Mj|vbBpxa_17TtWM^p}ODO6-qQWOq&Uvp(+b#i52Yh`(9d0%s8V|8+t<7;Jk`gtRB0b&nwWnV94BsqCs4rCW~a%Ep@WqECRHF0HQb#i52Yh`(Dd0%s7V|8+6HEv~jZFygFWn*=6WnXJ$d2M-L4`j%6a%Ep@WqE9QD|2OIb#i52Yh@E}d0%s7V|8+6Uu$J~ZFygFWn&+8WnXJ$d2M-Lb7f<7a%Ep@WqHPVUvp(+b#i21A8dJTd0%s7V|5sBUu$J~ZFygFWn*=6WnXJ$d2JnC*kogMa%Ep@WO?B)TXP&^TyZOfYHuDEZSgdO8SzcbS+Qmc6bglP78em65G%1@4j&LJ7Qbc_9uO=8zkL}HG8VsP1|9%98_avRcqOT11_p3tUu#8KmvLhN5fL050%5UXG6V`N0d!+^ayDOUWr|aIUvuSSt$%CJf9WCRc!PUx?0@@jh+}=IWnsr+v1@LwZB*oM@Mo@9YqV=^rfo&HZFS;v)_L_;pn83-Y-M+QieGbOV-G|fI}At`9UL)J4Hp3d7G*?A9}F5g5ef_*Tm~=(N**5;Dgzcw7ajyW080uT7&0CN5nB)ea0q01ZFygFWn*=6WnXV)d2M=Mb7hdpa%ErqWd&^=UI}Gmbv9)JKV^9kcq?;dV|8+6Uu$I(Z+TyHWn*=6WnXJ$d2M-Lb7f;6cV%B|WqECRUvp(+b#i52Yh`&6c=U2*V|8+6UutCyZFygFWn*=6Wi@GKd2M-Lb7f<7a%Ep@WqECRUm0R!b#i52Yh`(Dd0%s7V|8+6U%+K~ZFygFWny&(Y+q|-d2M-La}Q~Ca%Ep@WqECRUvp(+b#i52YXN)4cwcj6V|8+5U*|J@Z2(_dW-SMIWnXIo!E^kyBHjH;0ApWkWeZ?=Uvm~=b#i5YOBZQvd0(kvE*t?CEq-NrZ6aTDWf5m`WnUR~d2M+-a%E$6a%Ep@WqECRS#xD$c5-E3nA>@6dB}4SVs&z5Uu$J~Z4+N}Wn*=6WnXJ$d2M-Lb7f<7auHu^WqECRUvp&%cXDN4Yh`(Dd0%s7V|8+6Uu$IzZFygFWn*=6Wi@YQd2M-Lb7f<7a%Ep@WqECRU)X13b#i52YfyO*cq4KTWOZ_7Uu$J~ZFygFWn*=6WnXIncoBIyan53Oa%Ep@WgTx4cXMR`cNS$kYXN!2dtY;9V|8+5UpQr2ZAf1LWE6LEWd>_xd2D$ma~)tTauQxbW;YjbZb4E_MO;;JS{Hb2d0$##xpM&uJOBU<w|*WqIx0IiF@<0@HZC#%ATcp8Gbn{&1{MPsIuH>&5DH9Pv0(`U3oEH)5C(8%Uu#8KA8B86Wx0DB762Ox3mGOh9Xb{U7Z*ZnWqA*IUvm~+b#i6jYq@Y@_Cor2_XFh{&K1EAx?X0YLRz7FU*`(Fc766E`WgE!+Ch(ZN~&T>?=rM(K!s*sVP39eLydZ0nFe`fUu)KHENWb`c4jngVmxYPd2M-Lb7f<7a%EO)WqEFSUvrk>baG|LYixNLcwcj6V|8+6Ujb)%ZFygFWn*=6WnXJ$d2M-La{*!zZ~<HwW#Vn*T@+>)b#i52Yh`(Dc{O)sV|8+6Uu$J~ZFygFWn*=6Wh-lCd2M-Lb7f;6c4c2{WqECRUvp(+b#i52Yh`%}ee-tCXLWLAUu$IqYz1B!V`Fu4WnXJ$d2M-Lb7f<7a%EouY<X>YUvp(+b#i52Yh`(Dd0%tRV|8+6Uu$IqZv|ZeQ5Sx4WnXJ$d2M+$e`RBJa%Ep@WqECRUvp(+b#i4pZ5ey^dBSndVs&z5Uu$J}Z4FR!Wn*=6WnXI%X>EC5b7f<7a{gZrVg+sDUl(l`XL4m<Yh`(DdBk)0X5MpUUu$J~ZFpY_Wg2x+Wh;MWd2M-Lb7f;uau;|OW({I_Uvp(+b#i4Zdu4fTd0%s7WA1VRRu^UBZ5>q)X83gmcVBB|d2M-LbN*xKbk1IDWqECRUvgzSbrxkJXd8MIc{_6$U<+{)UL0isZXjO-WJ-QKzgq_u77GJiUJ)5~UkqhG%z7VjUvp)-a{&=M4i^izeJd6n7Y}+4HU|k=KtO+qU^5y35q}YQSsEBDQwJ6X3q?K!0a*nYEK>&t5FAB082}s!S0!K|5eFR?e+?HL2oNz8MH3nT5r2_qLrqXrsc#Sf5EU&11{@v=g>V-Z8>nFqA~if8abI&~xo`myEdmvzZx$@6V-O4h5jqAJdu@4Nsb(=SHosmIzi=o4JQfuf932aGZx>>1d0(kx5fA|oGatWt9S}PKYGZYB7F%m&c}-b=Qx|h}a%F{L4iEtq00RmU0RUBBYh@m7d0zn6V|8-nUz=xjXh4Hve)MbOdxvIr={eyH({aOd>RFFxO{IQh$V~KHsbP4?RP;u*XiA4{W@mWqS(|BjVr<YJ><*%QM2=-ds$*K$aJ*=Hu4z%^Ebt`ZSJQUGaH4a0ziD2vbx!9t^Dydg#~=M4y<Hx+M5AV+cN)HFKb?GEe`=e7bY)Y1mw9Y_X0L5-;bHY!yKqs(ZTEG}0mWn0T;C+gUa3(;vTIGFZD){`dTe}Vi57cxa%J5qZ#!dooqcQ}OL3=2b|*k?yJmJLU3L*=Uu$J~ZFygFWn*=CWnXJ%d2M;D-(+KT<z+Z)0eH`NB6AsIF>*M^Yh?s%a9;;xV|8+6Uu$J~2YX+0Wn*=6WnXJ$d2M-Lb7f<77H2zX8F&hMD|2OIb#i52Yh@E@d0%s7V|8+6Uu$J~ZFygFWn%$yWnXJ$d2M-L8DV2}a%Ep@WqECRUvp(+b#i524`J14(pz(7V|8+6B54_T5qmXtWn*=6WnXJ$d2M-Lb7f<7a%CxM7d9DiUvp(+b#i52A8&bWd0%s7V|D3eJ8c<w_IW#W5pQ*JWnXJ$d2Qlf?qJAta%Ep@WqE9QBXR+29$IBz8FLL{d0%s7V|8+6HG5@wZFygFWn*=6WnXJ$d2M-L7i`FMa%Ep@WqE9QF=`QPb#i52Yh`(D6HjwxV|8+6Uu$J~ZFygFWn*=60aX`d;%yyN?q<kza%Ep@WqE9Q)9GPj401+aA9s0ed0%s7V|7+#Ele1C8E{{7Wn*=6WnUk0d2M-Lb7f<7>18`-8F==2JAN5p?s5@RYh`(Dd0%s7_;v4N^lD{!ZFygFWMeFH0bdqo2X6J47iAuH3}z^55_uJR26GZ(Tzo5bZJ%)!NN!#i1_d3zS04->2n#742Dxwo7cc}7qiGr{0SUQr1p+!BzkC%RJQh*8b^;DK5o;9$3M*a=4F(1TGY0@2ISYStWn&L{EHM}n7y%VF9Rfp-aZ7PU7fWq<UkP#(9u-A41r`kq6*E&EQbb=DIvWaEKma9w6$lbi3^5oH7y%W331&lB3m;7_1P}onJ5v!1RT~Q|9|RQvSuIy(V|80@Ely>5Z3}sGWn%|bWnXI-acy~D0cT@%a=%_O7gcR}Uja;Gb#fPVYh`&KR9|yt5ngg-UqWG{d<!}P5DEtu0RS5W8U`3R78bd30t7q&1Re+radTy32YqE<YZiTNd0$gSLsbBEUu$KfeGoAK5ds+=Ixh+a5)2+X02f|$a%CuMWqBUIUvp*Sb*Oy}yJ2j$YJ2-)lXrY<V7G8)`X|mUy>erseRsn`seMa>WJL4|;~Il}MD7ykAggeCfqP&{W$izmbzft0`xEU5#s;)@Mx{??`Eu=X{bb7$*#yxn$5hi+qH}4#bxyTvMe7f-W?H#Reey8;Fpq6gwqZ(vOMUV%{4oE2%{1LR)eO6PK)G#Yi<EeEW<aN(d3k+ct#f2*O0H>6|2F9;sYY1MB;8BZ9orPi4#j@UcC%+svQt&GbyI?`aAayqh!#g{WqIa1N-;)Zw^3{ycwoChWE_29pnG>FOl}5wZFygFWn*=6WnXJyd2M-Ib7f<O;$>fJ@_A%=D{^IHb#i52Yh@E}d0%s7V|8+6Uu$J~ZFygFWn<oQWnXJ$d2Iw=2V`S)a%Ep@WqAjEUvp(+b#i52Yh`(Dd0%s7V|5N?^lD{!ZFygF7-9)?HeX0(4QqK{b7f<7a%FpK7j_VPJ8~Ie?sE8D2xlN|9bXP-9d{vRJ8Kww6MHCf5@QW<JYO7SP;WOSW*`v<9T$HY01Y1yIt2_35>hM=QAJQ`3rKTiW3PDvIv))d9t|-P2nMfz0y-ZJ79I^f3JU@l7Z-ACWqCw;g?kMQ1_ld01^}aH5HBnQ2N3`OEEpGdZFye+W@B}7MSn{dX>EC5sbd5X20Aty7dmZuU-)HXbpb73Yi0RuiCuPJNU33bh<HG#eq4-TLhF65a74UtP`qq*+fA@wLG4wuYGA!_MvJ*<VSr^`Zcd?mU;hHd0Hu9TiepcLoqAq&PMHR4WnXLOQ$Tt0dL(9c#9<z5X2WbaT5zOea5G?B2xWO~d0%s7V|8+6Uu<Q0ZF*mGWst#eWncVd9c%<&2V`S)a%Ep@WqA>K^m1imb#i528AA<jd0%s7V|8+6D{p0aZFygFWn=Dg0bLhm;%yyV2V-M(a%Ep@WqI~_!gkJLb#i52Yh`$C4OVkyV|8+6Uuzk8#&}<IWn*=6WM3a<d2M-Lb7f<725(<$WqECRUvvIr5q240@MRrn4Ow$#V|8+6Uu*t(@O<=gWn*=6WnXG#4Pbd+b7f<7a%DATWqECRUvp(+b#i52Yh`(Dd0!V}$aHdLUu$J~Y<VkxWn*=6WnXJ$6McDKb7f<7a%Ep@WqECRUvp(+A7N!*Yh`(Dd0%s7V|8+6Uu$J~34Zi)Wn*=6WnUI#4Pkj-b7f<7a%DApWqECRUvp(+b#i52Yh`(Dd0!cDV|8+6Uu$J~ZFygFWn*=6WnUL$(rkHOb7f<70W&LTWqECRUvp(+0c2%gYh`(Dd0*&d2Ym)(Uu$J~ZFygF{$uEI&R%O}d2M-La%C56a%Ep@WqECRBXR+1-f(4KYh`(DOkWOXA9omjUu$J~ZFygFWn*=6WnXJ$d2Jn4*kogMa%Ep@WO)gBJ97bJ-f(4KYh`(DcwYx-V|8+6Uu$J~2X|j{Wn*=6WnXJ$d2M-Lb7f<77H%VI{(10w^m1imb#i52YGn;zd0%s7V|8+6HDzUaZFygFWn*=6WnXJ$d2M-L7iq|Ja%Ep@WqE9QD{f_Db#i52Yh}`Hd0%s7V|5Q^D`;hTZFygFWn%$&WnXJ$d2M-L=w%0Z4rat_0e2aHUvp(+b#i52@MYv^(q40AV|8+6UTYD0ZFygFWn*=65lL%hd2M-Lb7lB-7HT7C{&@*^D|KaKb#i52Yh~hX<XYHdV|8+6Uu$G}6nT7eRAUBn5?yL#AZ>VGa%JxV3T6gt5_m*u5gKT8b#fPcYh`&CReu^5LlhntItl>*O%O3t5D*YtMIIj!8~_O`8Vdwf1`2-}015&XDHcmjTL^g!9|Q{-5HS=*H9IjyEDjeB2n&B43qu7R7b{B_Ky7(n340YA5f(Zb6C58|au^H`8B$+vOIJri9XbU{4FDbqC1e{`Lk}?!N*e|S1T7yB2^VD?918^;6%Z`~3m#1YEC&P;0S6U-4Ga|sS8-jxVgd+Dd`e0i1Q&1s4QUMk0X<7WF(Nb?TuVC#7Zxxc7a9l(RR9qJ2L>HE2mnn@UsVZg039C+J4;RhO#@Q}3jhWe7by-GSyxCUP%|wyQWiQH6C58|EC&P;0T%&(7!Vo`94r6>78xEKe+m&<7k_0&TvJ3`A9E@O8VCw3QxOXgQZo@KMG6QDDHaz)009g!3`H1CFA*?B6&x25IvGV68CiCG7k+heWi4rCd2I`Hb7f-(US(fv7fEe-U#Vmy2U}%dYZp^(d0(kv6BGswg<${z9T+he5D*XmzgZ3)5FQOI0bgTva=%*y6&wQ#R&!-z2Qg(|YfOC~VqbG*xp)c|D+(747zqFa1Q#8sWH}ipd2M+tcV%OBQbm7D7in#IU#WEv0TUN1G!qvNCM*^g6%YUy5^H67`FUS+7I1WOW#4PPa$@-#uVQxP7O_}xxp83aOygklAnH-aO|@AewGO)`vwI@3S30?IeCd1tYQJ%N=?>#2sbW(1H_cVWVbKoTCaGsZi+5bVadhGq>MW^aSBrN_mveG(Nc<w`Dy~aaw0BdYLT9*fK<zYxcxdcG`%=(V>__!fi+D}HeSh&z`(~+rR_k)j5T$%pi(^rxU}(=?#c-j2K=*pRbzt@w`XaMoHL+78l6q}-d6#Wz`g`nF`z+xA;Q*s|PN8~ByKiIuB={El3%7A^xlVlcVeK=6cWmz@`X-NLSIJk&bISv#B(f%tVJ)p`FoSn&?<D#rk7QoKC&6R06R#AyHjiO6tZ6H#d}VD@qG)=N7IkfTU$A3wFnng3Wnesdemrw!V|8+6Uu$J~ZFyRAWn*@7WnY-<d2M;fa}i>7a%Ep@WqEB4U2|n)b#i52YyNo&cq?~hV|8+6Uu$LJZRA|oWMg%5WnXJ#c^Q6Rb7f<7a%EouZFy~ZUvp(+b#i52Yh`(Dd0%q@Vcv6PUu$J~ZFpY?WMg%5WnXJ$c^PwGb7f<7a%EreWgTt}TXSV&b#i52YyNrgdh~K-V|8+6UutClZBSc1A9W@M3NITB7YbPkJtjj27Z)iG7gs}9C1Dc{76AY)9RLeWR5Th14^>E1B}+3mE?F!V7ZnfyMJyi*2^}0eQx+B$5dbV00}KHbCS6Qr2XJLyYrl9u3v+X2V+UJhUuzdrZFye-BV%=P%wHLHd2M+uV`XD?sA?=93JEd~F%UWs5C9W885byRd0*LOV|4*iUu$LgZKYd!=`#H>wNOsM7|kk=c}%x)Sh-tm;xOzmk9|kCaZ$NjV(BR5I*)ux*L2zzk6~7<X-zF)Wn*;_WnXJ$d2M-Lb7f<7du3m1W_fLStVLyGb>(F%YGrwCd0%s7V*znxUu$J~ZFyf8WCwQ^W;<^Ie8GS8c4cFAa%Eq@WO;3QUvp(*bqi&7Y%3VQcwciq0U90we;EKBFmr!XMMG6mMSn|0Sxs4gQ$<5nQbm7DMOjT*e^W(6RZ>M&MG7f27I9NWO&TIRFhxaKO<8|aMMGO1H3kGrSppU?T}4AxQbko$MOjT*e^W(URZ>NNQ$<-#S$|VSLrqdee+yk%Rat)%T}@R|MO6zt76KM=Qwm!w9SRRjMOjT*e^W&aO)Cm8J3?7iS$|UnTUAm;RZB%#O&MoXMO#%;MSn|076KM997RJ-Qbm6Y2U%5Fe^W(URZ>M&OGQ~tS!Yv4TUAm;e@jJKO<8|aMMF(eMSn|OSyfqoQ%f^dQbkn@JQe~ecvD4NRZ>NNOGQ~tS$|VSLronDFgrq7RTeNDLPJ$jMO9HtS3_5ENncG{NMB`9Uqe?zWl3LITU<+VMN30NS8-iSSx-n`RZ(9<S3_k<Us+E`Uu98WLsvs(Nncq{NMB`9Uqe?zWl3LIPe@-?QC~w>LuE-{Sx-n`Wl>*4S3_k<Us+E`Uu98WLsvs(Nncq{NMBV;MOjT*e^W(6RZ>NNFb5U^9e)H33IP{5e<mb7C|MmUMK~872|G&{90?>0BSkPhGcpe(D<TgTGZ#e~5FQCI95`7`S++`LV|80+Eox<XZID}YWn%zLWnXJP8v+$OQyc~v9ttQnfy4S)1Q7}k5mEvz4geQ0J03kE4>UF)3?nRAIXoUdMK~872|G(1903(D1UQG!<sVfE3Ka=iH~|0#8(U$8ZW0g)4L7M`6BHH!HU$EsXbm<82?nos7Aq1797KDCV<!(35e@)26&L^%IsrN%5ddaiYh?>Pd0%rEaCLHJEqi5oZKG2^3IrN0Ha7|q2?7@_DP?1I!ew7;7D#P*U-M<Zac1!fn`LrMK3;=!V<&SlUb{FOoq1m#WC(YHWnUd<Ic|+ecyl3khh<c5CVC%gUvp&ub#i52Yh`(Dd0%s7admQKTx(@{p0`|cW%P9hWM6A#d2M-La}Qy4a%Ep@WqECRUvp(+b#i52YXNx1cwcj6V|8+5Umsw3ZFygFWn*>OWnXJ$d2M-Ka}i>7a%Ep@WqEBAU2|n)b#i52Yh`(Dd0%s7V|8)?UBF~{ZFygFWny&(Vqa@zd2M-LbIxORa%Ep@Wq553R&!-zb#i52YXN#0b6<01V|8+6U+`rOVR>J3Wn*=6WyEU%eHn9Kb7f<7a%EreW#nkmUUOw*b#i51YY}#Bd0%s7V|8*7PHSa(ZFygFWe0E=c3*2{d2M-Lb7f<7a%Ep@WqEBLUk7nxb#i52Yh`)%dCqbHW#n@aNo!?!ZFygFW%zaDWIJs1co}V9b7f<7a%EreW$0`jSK?$BVRB_(Yh`(DdBk({Vi9}vULSFJZFygFWn*>eWzK2=fBbkWWo2V^a%Ep@W#Vn<UKeljbOv!>Yh`(Dd0%t>W8`xIRQhBMd3j%RWn*=6WyEXrcnNjRauIiRa%Ep@WqEDlU*cp3bK_(yePwxVd0%s7WA1YFUJq#KYz<3uWn*=6WnXLldHi@gd-P%fW@TS%WqECRU+87>bQWvQY7uR1d0%s7V|8-=U;1PnYv^7Fb7OUKWnXJ$dG>kEash1Qa}i5xWqECRUvp*nb>n0^VDxwyZC`U`V|8+6U+`t<Y#mSHWXN=KWnXJ$c?oDMXJun`a%Ep@W#VleP3~t0W)^Wfe#vjfe_wNDV|8-QUTbA}ZFygEWomT>d|zv2d2M-La{*uhXk}k(WqECRU+85Aa|U@|Yh`(Dd0%t>V-aN$MQdewZFygFW%zX#Z7X+Wd2M-Lb7f=hasfvlZ+UHbUvp(+b?Id*b!B;Nd0%s7WA1VRMju6aZFygFWn*>eWjk>ZWo>z1b7f<7a{gZre&l`9UUOw*b#i4QYZ-Y7Wi(r5V+VN=d~0QSZFygFWyp1MWnXJ$d2D$x2N`1#Zw_~BWea8vdUIuCb#i52YtDIXd0%s7V{~#0I~Qdga}sxRWf5EkLSJiTd2M-La}j@aa%Ep@WqEDlUl)28YjR~@Yh`(DdBk%ON_BE&Uu$J~ZPH(JWn*=6WyEU{b8UHFb7f<7a{gcTVA5=PUvp(+b#rAgT^V@^Su|T^V+U&ycxz>OZFygFWfy63WnXJ$d2M;ba{)pDcx7K}WqECRU+882cG+ZKYh`(Dd0ulIV*yoVUu$J~ZFye@Ph)j*WnXJ$dG>ibQ4wi%a%Ep@WqEDlU+!kebaG{1Yh`(CdDFX0Ks%^lJO=<69|K|w0R&hb6*>h)5g83H0AEa61rjJl0~ih*Jsb)MTM-H}L<$Q89yT2W4_hW2FAfJ59tv>=7fllr5jPGO3ut*?a}XYNa%Hdf_3EAE&;6DD<@}Yx`|gSG>CID>{^k9Z!u#=w@af)z`1AgP_|M~&<o)Zf?)Bt_@Acc8`04IhukQ8Yh41q7OO@pP_^<Bu=!Ng~-<$a9?}@_W??Z*}_0603>EemP<K>g+;_0vU_4S?P&-a!7<>N)K_VxIk<j?TGW3O{Qg=tkt7kdIzA95xpBn>}BFC#jCARsX#H#b$WXGve9UM?SURUt7DJ4G)eI)5M_F(WrORk3GDUIR}cEi58ZEDuX0Jt-?1AU0{Qa8+v&V_7I67AJ3tU2<h#5pOLbHWMI4E-*YWg>42L0}VO>OkoFeWnXKIcx`!KsbB;L7XUFrU<){TUvn2Ub#i5eWflw%4K@b}1}YN?HVg|3J9%Go7dv%wWh!W8d2O4=_8(|0JunSRCNUx~95xVTb#i6B|M8po_$qK^V|9@G<QYMEZFz-qRJn9Ozg}1$Ycw_rAw?=BQY0HMH#|Nne@R8TbVeUlE*%gV5HS=>O<M>^76lU+0T4S=1`8S+20BGWDFGZl002V<7YRBD5m^jbDG~_^5mE{-9}E@)S9WC=N_BE&EkR{@Z3|*^Wn%{@WnXI-Y;Ad80ZC(Za=%;{3=6k>JQfiG9sp)vYh|Np6EGSJxpz5Ng=sBIw|q7o6&3-gU<e~DEhq~ab7f-(J!M~Ozj!YT5_4r^2P0))YZrTMd0zo0V|8*DbZcdKM0kaD1`8S+209pId2M-r0d-?_a=%*!1P}uYDRX6G%5r627^!=0dEaxnXLI!|-XiTDxqV5mVRxZ+bAxYV{v`MoqiZgqb}NH#b^RlyTYK$M`4jC7|90tUiC=SbFn5M!Uq5FoZ;4-XHen-hm0xRbE^m!rb6`7nu3=W^K#pyBP7!C2b#in)Y4J<_U9WRxau;y*KAUBEd>dWwXY&DqWnX#+d-Y4Nb7gWDaQQv+F^O$?P7!CrXM$y4dIx*SJO4+OV|8N(UAsa+oq1nk2Vu!j-AkKgd3+mP%QTa9a&$du*$dSjuXAN`7jUJ0n`L=?8(p_IqcMVIUwQ|7rFgG%WpWpAsePkyiEVjK5ofbFEtOwubQ^E2KM}P&7J_A8dIx*G8asn!V`LC#iw***2@$VzWpWpAwKoBkd2MJtaj^&(q7N~fWqEuXU84&Vg>q$131_Vw3XcO3lXY@*J!zGBZ46#DXOneubUkU2d2K#jI%ku0awA<KXNhfjP7!C5b#gCVAZLkfc}@{$mvwR}T_tCUZFv-NDq)3kWljlaiEVihaWr9ta%D~lXN_%n4RJAHg>q#MX)t@8d0%1&VTE#K3TZQYoq1nk2VsG7We90Jd!2b-C1*Kzf@NQN2Ya1)Unyq-cZOwOdIx)*d0!f52zQ2MUmj-;Z;4-X5n&B*m0xQedoOygb7c{CF=nr8Wh!nWT!Up}5pfJ$n`L<)dMI#_V|95PT%TomXaiiUZ*8e#bH{o4JoQfhQo$nCLB%}BK+$^1UB^_@R>D4;dZl`)IG;eJ1-T=w9HSPkJ}r+SFtZ>fwMa9zXf*Lzt8Q}TA@5?hX=S)|L91wR<pJ*kw`pRybwaCXaODB-0=H>s`6$mYwRBwGME7{fFUBGFInffu5w%TGuyt0UQegEE|1Y^ydhsazI?oBgLe*ilO-`|OOQBO@fp28yHqS1#U@N^Yvj($gII&Y8m0)dhPyu#hb#hEzv3D&63px@3Ga4NU8WR8-7!5E124i({WnXJ$d2M-Lb7Et4a%Nv^Wr`7FUvu(f0dr+vYh`(Dd0!c4V|8+6Uu$J~ZFygFWn*=6WnaK$d2M-Lb7dZN7Gxr70ecX8R&xPh2yqcwYh`(Dd0%s733GB~Uu$J~ZFygFWn*=6WnXJ$1#Z$_b7f<7a%CH9>U|D-ICBPJC}d?{7GVWx6IOF&V|8+6Uu$J~ZFygFWn*=60b9Uid2M-Lb7c^8{%|92^n2l9TXPs@2zD7-FJ&YGd0!4=7k+YOUu$J~ZFwtqWn*=6WnXJ$6JdE@b7f<7a%Ep@WqECRUvp(+AAMzCYh`(Dd0%s7V|8+6Uu$J~5qcwa&S7<OWnXJ$9ca>Bb7f<7a%F037<~zUBXa&@5q0=n7GfP`1zj3s9(@*VBWVnH5O6zs8D|`G7*!W#6MT7Jb7f<7a%Ep@WqECRUvp(+33VA(7jM;P(p+<8V|8+6B48PL2WVe&Wn*=6WnXJ$d2M-Lb7f<74q_u?8FRsN^l)Wkb#i527HJ)A9bXq^$aivOUu$J~Y<bfHVPkx9Y+ny<1a1vlb7f<7a%Ep@4}WcWUvp(+b#i52Yh`(Dd0%s7A9mSfUu$J~ZFw7W>Sq>k0$&JcBzt*Z4q+d07;Il_WqECRUvp(+b#i52Yh`(D9aGq3V|8+6Uuzb4;cO#!^kMmGVP6(t1Zf3YH)TE=a%CcI5pr#LUvp(+b#f6~Yh`(Dd0%s733+m5Uu$J~ZFygFWn*=6WnXJ$6JmK^b7f<7a%Ep@WqECRUvp(+32_-&z-M`Fd0%s72XNVEUu$J~ZFy>Q7-tc58D8*Z9ctuU4q^v=4rexM7;y=4BXJC32zvom7hw==1XT}Z31o6*Uu$J~ZFygFWn*=6WnXJ$1!@IW4{y(Z*=ApBWqECRB6t~NA7f=-Yh`(Dd0%s7V|8+6Uu$J~5q=|k8EM&g&RlC{d2M-L4rvE<7G*nY&U<ZnUvp(+baLq~Z)I?8a9<Z_9(D#`Uu$J~ZFygF4`p?7WnXJ$d2M-Lb7f<7a%Ep@8G6QeUvp(+b#ftJ<Y5|b9$ye=K4WraB5xUe2XJ3=Wn*=6WnXJ$d2M-Lb7f<77HRZqWqECRUvm~>`DYnh`e*fZeP0e>9&rv}8*4ZgZFwSf5omRCWnXJ$d2J0_b7f<7a%Ep@4|Q#MUvp(+b#i52Yh`(Dd0%s733_s6Uu$J~ZFygFWn*=6WnXJ$1#Sgd*k@yPa%Ep@0er@LUvp(+b#hQ&7GWK01zzZ72XgObB5VP15qmar7;6!F8C?Qo1Y{jn4`B*)4{sxD4`^+9Uvp(+b#i52Yh`(Dd0%s7A94<CBVoyN#(H0KWn*=67*rQ!6MT7Jb7f<7a%Ep@WqECRUvp(+33VA)7jM;P(p+<8V|8+6B4+`433)qn&S7<OWnXJ$cy0AAcV%jIdu2Oi7<w6eUvp(+b#i520b_Y>d0%s7V|8+6Uu$J~ZFygF8DQRXWnXJ$d2Kyk{9yoh6=ghWIB#uvB6k^QAA4nAYh`(Dd0%s7V|8+6Uu$J~33c>xWn*=6WnUO%^>_ta;%Dz|c4Z=N7=00Z8*?}eb#fS4A8vVVd0%s7V|4~$Uu$J~ZFygF4{vpHWnXJ$d2M-Lb7f<7a%Ep@4|Z*NUvp(+b#i52Yh`(Dd0%s7A9fC7^l4>zZFygF0cPHCWnXJ$d2LKz4q*p#4rIh@0e<j$B6I<332+Qv7Hu761zj3s9()#TBX10N5OX7Q4{~*KWnXJ$d2M-Lb7f<7a%Ep@8GaFPBYDYb-f?ALYh`(D1XK@Y31o6*Uu$J~ZFygFWn*=6WnXJ$1!@IX4{y(Z*=ApBWqECRB7Xs65pn@vz-M`Fd0%s7Vs-u$TWf52WO+M$7+?W+WnXJ$d2M-L8DnF0a%Ep@WqECRUvp(+b#i527iQ9Id0%s7V|6xV&~FBN3VA$nICXV$7+V)%6J&W`b7f<7a%Ep@WqECRUvp(+5q{2IYh`(Dd0zlz?_dsL&S~jkX?Y@c7-tE0AzwBMd2Iw)2X13^a%Ep@WqBEWUvp(+b#i520cm+{d0%s7V|8+6Uu$J~ZFygF4{UXEWnXJ$d2M-Lb7f<7a%Ep@8F~?a^l@clb#i524`9-7d0%s7V|7PmB5whI5qQLN0c7ZL7+4Q&1#b{u4s8d04rexM7;p)2BX<m92zVJ^0d#q7d0%s7V|8+6Uu$J~ZFygF8Dt528CAz`(r$TQb7f<74{jrC4`^+9Uvp(+b#i52Yh`(Dd0%s7A94<DBVoyN#(H0KWn*=67*h{r9c>+7*k@yPa%Ep@WO?BTTXSq<d~yL#7G@1-d0%s7V|8+6HEm^iZFygFWn*=6WnXJ$d2M-L4`#@8a%Ep@WqB!i(02x55^@GzHgkDx1X~Yb34C&8Uu$J~ZFygFWn*=6WnXJ$9emPWb7f<7a%C)P>1+{w&T;8`adH@17GVWwJzp*gV|5Q>D_~`LZFygFWn%$$WnXJ$d2M-L8EIp6a%Ep@WqECRUvp(+b#i520cv?|d0%s7V|8+6Uu$J~ZFygF8DI%?&RuI|d2M-L7huSDa%Ep@WqDY6B6k6033L8m4`SqQ1XvesA9ovMB4Yt@5qmar7-|uF8CwEm1ZM?b8FXWHa%Ep@WqECRUvp(+b#i527h(lu1y$c~$aZpNUu$J~5OO1P4{~*KWnXJ$d2M-Lb7f<7a%Ep@8GaFQBYDYb-f?ALYh`(D1XCAf2Xz)@^l4>zZFygFWMlaQVP9fpaBUr24rUi{a%Ep@WqECRHFafUb#i52Yh`(Dd0%s7V|8+6BWTWeZFygFWn(dN>RSkB9&H+3E^}jb4`Cy34{&XHUvp(+b#i52Yh`(Dd0%s72V~h~Uu$J~ZFwwm>2?Wr^j+tDeQg9<4q+c~He~_?WqA;PD|lsNb#i52Yh?{-d0%s7V|8+6HD_gcZFygFWn*=6WnXJ$d2M-L8ERv7a%Ep@WqECRUvp(+b#i527iI-((p__9V|8+6J8sT<ZFygFWn(~c7+Vix1#IG97h?W)4`MrG8G8hHB6|UA32+Qv7Hl141zQ?q9)AvHHF{-vZFygFWn*=6WnXJ$d2M-L4`LsD4sY{e&U$TmUvp(+2zeP_0d#q7d0%s7V|8+6Uu$J~ZFygF8Dt518CAz`(r$TQb7f<74{1AV0eJ~|^l@clb#i52YGw5teP4QIYIPQ7B4`nOZFygFWn*=64_Rwvd2M-Lb7f<7a%Ep@WqECRBXG`Qb#i52Yh^uc_FE8V1a%Q-0)1t95Pc(e4{CLCWnXJ$d2M-Lb7f<7a%Ep@0e!}JUvp(+b#fM7=WqpS=w1JPXLS!?B5xUdDR}}MWn&0*5maksd2M-Lb7dECa%Ep@WqECRHGgGeb#i52Yh`(Dd0%s7V|8+6HDqOZZFygFWn*=6WnXJ$d2M-L4`v^8*=JvCWqECRJ9f@tb#i52Yh_Gr1X~wlA9U$uJ8bxR5Pmy*8DSiA7*`K%1#b{u4r~W}4q-NG7;_PMHDYCBb#i52Yh`(Dd0%s7V|8+6BWxLP5p(l-&R}(NWnXJ$1ZD+a8FXWHa%Ep@WqECRUvp(+b#i527h(lv1y$c~$aZpNUu$J~5Oq6q0b>zz&RuI|d2M-La%JxXc4by;Y<UT5B5)CAb#i52Yh`(D6IpX*V|8+6Uu$J~ZFygFWn*=68C<|*d2M-Lb7d!W{b4+50(lO50%c`m2zD7;0c?3~d0%s7V|8+6Uu$J~ZFygF0dn4RWnXJ$d2I?_|8O61<7d-zVR;aIB6k^PF>*LCYh?s$4ODYwV|8+6UuzM4ZFygFWn*=64^wMpd2M-Lb7f<7a%Ep@WqECRHGE}bb#i52Yh`(Dd0%s7V|8+6BWM|a#(Q6LWn*=60b0Okd2M-Lb7fX_4`DlP8F==2J9PM92z3Eh7iSP`1XmYrA9ovMB4Pn>5q&mt7-<P|4^C@kd2M-Lb7f<7a%Ep@WqECRBXk*R33$m>z-D=Ed0%s79)1pGHF{-vZFygFWn*=6WnXJ$d2M-L4`LsE4sY{e&U$TmUvp(+2z~)y4`m%~(p__9V|8+6UTf(HX?a$2Y-15&7+fD<d2M-Lb7f<77-L^+WqECRUvp(+b#i52Yh`(D1zgx<V|8+6Uuz+G;(a`E0%I0%I7w?|1Zf3Z8Ej*9a%Ep@WqECRUvp(+b#i524|LLOd0%s7V|4*!(|#F!{Cm@DVPgn)7+V)$J#8c~b7dZL25w(#WqECRUvm*>b#i52Yh`(D6H{|#V|8+6Uu$J~ZFygFWn*=64^V4md2M-Lb7f<7a%Ep@WqECRBXAjI-f(4KYh`(D9a`9DV|8+6Uu#f#5Pds!8Dj2o0a*5C1Zo{u4`&K=4{bYR8G8hHB6<O833d!#7H<V@6HaqwV|8+6Uu$J~ZFygFWn*=68CVx=1!vV&*k)sOa%Ep@7;+JLHDYCBb#i52Yh`(Dd0%s7V|8+6BWxLQ5p(l-&R}(NWnXJ$1YsRt7i9-^*=JvCWqECRUUTUZadK>5Vr3n91Y8GTV|8+6Uu$J~2Y+94Wn*=6WnXJ$d2M-Lb7f<74rcUfWqECRUvnX2`gR6g3}qT`BuR5+9&rv~HDYCXZFygFWn*=6WnXJ$d2M-L7j(#Ua%Ep@WqBTW(`FfG<Z$UnZ)F5%1X~YaCv`6hUuzhD8FF89Wn*=6WnUj*d2M-Lb7f<77-?T?WqECRUvp(+b#i52Yh`(D6Hs$yV|8+6Uu$J~ZFygFWn*=68C(}*(r<ZRb7f<77GU&gWqECRUvp4n2zCKk7i8jX9a!#W9&#3KBWVnH5OF(u8DSiA7*-E#1!)jo4sRcI7<6B2WqECRUvp(+b#i52Yh`(D1y~PkAAjC&^k`*yZFygF7-$J{4^C@kd2M-Lb7f<7a%Ep@WqECRBXk*S33$m>z-D=Ed0%s79(fjJJ8J=X#(Q6LWn*=6WMAhLeQj`GdSwT84`wTFWqECRUvp(+A9Q73Yh`(Dd0%s7V|8+6Uu$J~5qk7;Wn*=6WnV94_Gubj6lDN+FLPgO7=00aHF{-Zb#i52Yh`(Dd0%s7V|8+6JATf1ZFygFWn%_&=}H%2=x_B$cV!-M4`Cy2A$c$sUvn5`0eNL#Yh`(Dd0z)%V|8+6Uu$J~2X$X_Wn*=6WnXJ$d2M-Lb7f<77;0Z@WqECRUvp(+b#i52Yh`(D1zZnf$aivOUu$J~34HW%Wn*=6WnW%p1Zf>v4`ldt7GlC^7=8(HBXJC32zmim7iSP`1XdSpA8{LGB4HVM2WVe&Wn*=6WnXJ$d2M-Lb7f<74q_u>8FRsN^l)Wkb#i527H$P?6HaqwV|8+6Uu$J~ZFygFWn*=68CVx>1!vV&*k)sOa%Ep@7<CDGJ97bJ-f(4KYh`(Dcwhe%XLWmJR%-!z5PB<iWn*=6WnXJ$6Ki>2b7f<7a%Ep@WqECRUvp(+331L|Yh`(Dd0#hW>~RriIBN!bFmGRT7-tD~4_0esd2M-Lb7f<7a%Ep@WqECRJ7vydb#i52Yh?;-^-2$6@^}7yTWc765Pc(dA!8^VWnUI!4Q6>?b7f<7a%C%TWqECRUvp(+AAV(DYh`(Dd0%s7V|8+6Uu$J~2X<d`Wn*=6WnXJ$d2M-Lb7f<74rU{5&U<ZnUvp(+5qHjAYh`(Dd0$3l9&r|9BWnJ634X$G7-SK88C?Qo1Z5pp4`&K=4{SSP8GQtJB6%5OA7f=-Yh`(Dd0%s7V|8+6Uu$J~5q=|j8EM&g&RlC{d2M-L4sIWH7<6B2WqECRUvp(+b#i52Yh`(D1y~PlAAjC&^k`*yZFygF7;h1B0bdVg(r<ZRb7f<7b7j*SVR>YER&xP#2yqcwYh`(Dd0%s733GB~Uu$J~ZFygFWn*=6WnXJ$1#Z$_b7f<7a%CH9>U|D-ICBPJC}d?{7GVWx6IOF&V|8+6Uu$J~ZFygFWn*=60Y|`Od2M-Lb7c^8{%|92^n2l9TXPs@2zD7-FJ&YGd0!4=7k+YOUu$J~ZFwtqWn*=6WnXJ$6JdE@b7f<7a%Ep@WqECRUvp(+AAMzCYh`(Dd0%s7V|8+6Uu$J~5qcwa&S7<OWnXJ$9ca>Bb7f<7a%F037<~zUBXa&@5q0=n7GfP`1zj3s9(@*VBWVnH5O6zs8D|`G7*!W#6MT7Jb7f<7a%Ep@WqECRUvp(+33VA(7jM;P(p+<8V|8+6B48PL2WVe&Wn*=6WnXJ$d2M-Lb7f<74q_u?8FRsN^l)Wkb#i527HJ)A9bXq^$aivOUu$J~Y<bfHVPkx9Y+nz21a1vlb7f<7a%Ep@4}WcWUvp(+b#i52Yh`(Dd0%s7A9mSfUu$J~ZFw7W>Sq>k0$&JcBzt*Z4q+d07;Il_WqECRUvp(+b#i52Yh`(D9ZuL}V|8+6Uuzb4;cO#!^kMmGVP6(t1Zf3YH)TE=a%CcI5pr#LUvp(+b#f6~Yh`(Dd0%s733+m5Uu$J~ZFygFWn*=6WnXJ$6JmK^b7f<7a%Ep@WqECRUvp(+32_-&z-M`Fd0%s72XNVEUu$J~ZFy>Q7-tc58D8*Z9ctuU4q^v=4rexM7;y=4BXJC32zvom7hw==1XT}Z31o6*Uu$J~ZFygFWn*=6WnXJ$1!@IW4{y(Z*=ApBWqECRB6t~NA7f=-Yh`(Dd0%s7V|8+6Uu$J~5q=|k8EM&g&RlC{d2M-L4rvE<7G*nY&U<ZnUvp(+baLq~Z)I?8a9<aE9(D#`Uu$J~ZFygF4`p?7WnXJ$d2M-Lb7f<7a%Ep@8G6QeUvp(+b#ftJ<Y5|b9$ye=K4WraB5xUe2XJ3=Wn*=6WnXJ$d2M-Lb7f<77Ju|=WqECRUvm~>`DYnh`e*fZeP0e>9&rv}8*4ZgZFwSf5omRCWnXJ$d2J0_b7f<7a%Ep@4|Q#MUvp(+b#i52Yh`(Dd0%s733_s6Uu$J~ZFygFWn*=6WnXJ$1#Sgd*k@yPa%Ep@0er@LUvp(+b#hQ&7GWK01zzZ72XgObB5VP15qmar7;6!F8C?Qo1Y{jn4`B*)4{sxD4`^+9Uvp(+b#i52Yh`(Dd0%s7A94<CBVoyN#(H0KWn*=67*rQ!6MT7Jb7f<7a%Ep@WqECRUvp(+33VA)7jM;P(p+<8V|8+6B4+`433)qn&S7<OWnXJ$cy0AAcV%jIdu2Ol7<w6eUvp(+b#i520b_Y>d0%s7V|8+6Uu$J~ZFygF8DQRXWnXJ$d2Kyk{9yoh6=ghWIB#uvB6k^QAA4nAYh`(Dd0%s7V|8+6Uu$J~33c>xWn*=6WnUO%^>_ta;%Dz|c4Z=N7=00Z8*?}eb#fS4A8vVVd0%s7V|4~$Uu$J~ZFygF4{vpHWnXJ$d2M-Lb7f<7a%Ep@4|Z*NUvp(+b#i52Yh`(Dd0%s7A9fC7^l4>zZFygF0cPHCWnXJ$d2LKz4q*p#4rIh@0e<j$B6I<332+Qv7Hu761zj3s9()#TBX10N5OX7Q4{~*KWnXJ$d2M-Lb7f<7a%Ep@8GaFPBYDYb-f?ALYh`(D1XK@Y31o6*Uu$J~ZFygFWn*=6WnXJ$1!@IX4{y(Z*=ApBWqECRB7Xs65pn@vz-M`Fd0%s7Vs-u$TWcJ74trj624M(x5?@GVNNoyU1ZQG(D`j45WO@B^(=i=jEOHWFNM(3!AYbEe@1hE325S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@B_)59HLEOHWFNM(3!AYbEe?=T8x25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@B_(`_AKEOHWFNM(3!AYbEb@5Tyd25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@B?)Bhb{EOHWFNM(3!AYbEb?^FtA25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@B@(}^8mEOHWFNM(3!AYbEc@A?X625S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@B@(;FRNEOHWFNM(3!AYbER?}!R!25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C5)1@6?EOHWFNM(3!AYbER?;Z+f25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C5(>EPpEOHWFNM(3!AYbES@2m=D25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C6)4?5JEOHWFNM(3!AYbES?=lKz25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C6(^DN_EOHWFNM(3!AYbEP@4yOX25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C3)BPP_EOHWFNM(3!AYbEP?^X(C25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C4(~lisEOHWFNM(3!AYbEQ@8k+*25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C4(-|FLEOHWFNM(3!AYbEV?}`d$25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C1)2kg|EOHWFNM(3!AYbEV?-&YZ25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C1(={DnEOHWFNM(3!AYbEW@2(1F25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C2)5jfPEOHWFNM(3!AYbEW?>q`-25S;{4trj624M(x5?@GVNNoyU1ZQG(D`j45WO@C2(@`B@EOHWFNM(3!AYTe)8+I#YC~8b%BLi_uRa8JnR%}{PNLM%>I}|V=H&YW{96wwuYyl)MB_%0oC?6jII2a)-TOK1l2C;8XR7q<?Q&dDpP$g_i3JDrM0Rb6tToET9zk44WC2tKE0Rk3fL`oPP5OD_p4-gd>J_bt`A0BWK3KtK5N-Pcw9Vr$(1_%Zl2ESMc4Hy|FHW$BZ5gi691^^csP+h5E2NVVbg>C~70URs|bxZ~p20j@9Rw))J9SIB+79U(i6#y4tZ~y@S6aWEmFA5F=6)+M3Od%HuIt&*W00Tf=76%p+7du2T9043S0R#?OCIB-I0t*Zje>Dsb5CI={L>3(m7%dk{G#wKWEGiWVLNq!T3<6pu4L%<hI2{RpHwpj%9{@2Q76WxwEEfg>2Np^jC@eHWDm(!I1{(nlFdr5JX;(D^0vT^z7CQ(83kg;a8U_~t001mRC>$ONIvoNA2MBy{7y%j#3p-pj3Kj+sEe;k|IUF+<0udA+A5TOU9S#^R7fLf65fLgG016j<aS{~>4|Yp71_A?PRxB3=0tXgK9SQ~#7zrhJOBEIrA4NnK9S#^R7fL4@5fCyC3k@DtFB%;N89oF(5n)#y7dTpMxqSctE*=018487T76t|Z3@`;3P;Gf%sbUWt0TDX_7o%kyF&7pT90m<7A!T`O3m9`{V+S2&Uu(a89TqGHOl}AAWnXK*a1RzMED;PI7Yi*AWqEC*Q~&`06aWDL8w3pn3lno?W3PJyHU|JE0T3()zh@I02|BT63?CJRb^!tb6IU%3WqEB2A#-J8uW<r8AHRJb95DwLZgp~He@jJKO<8|aMMG6mMJ;<}d2ORx000{d0O?<AWv*>`UjPAab#mojw`py<bwi?Qf2MwW-z>dpE%_F!YkBoGm0Mt7X|-=a`)<EgP{LKpZ_!q*e?+!-JEKKt^HjlH#%0Q1qZ6lI68SW#O-|Q(wRbzIaYExErF?A55%L7&74kFs3E5W3TcC4R#RjoXSEYEhZ*9X|(_YFrkAE)dZlOq1#YClKPtR_>Z*tj4qi{;)cD+bS#Yp`Y&vw0aXypmc2gORoE$3$S52j>V&uG1FbM7PJ8N)W(0Owxy1-@<`<6)F|a(808bVZzcUuJugV|idtvvX19a)VPx#DCLo_fWA}TB=Jvv_nGbROedSL)1f`7O+@3;53g*Qt@P|OFq7LX!;?8dT{Lz?l|HC^cmv`|4`L^zHe&75w~PcrCzghOWi>4SlvFQW-iZYy>3m}c%ySk<#)YFbj5DHY<A;eyJAztZu<)9XrW1N@(<)5#cabd!FcI2pmSX1alJ@&@&)__|1ix4%}4bkxN<oCeW-qAaY&+cW141pcxSI?Zf0ewb8h2qrA=G-dBkbmNwI%iwrwD&e?<LK%|qH{(qFj<tYkm;GNn>d*J8D8Afiid?I)>YaLWnu9{e82AM_8^N!44pb4=Y0i(*-$bgFZ0+g!;;!2+XkDCKdzNK3_Dy>E5nV7p^&#YnqwQ2l*}WJJS6;tJ1hy>D>tGvW!uM%ppwe)Sc;Z(!qQyJBqeBl;QHF3~#6Q1c0)avu9(j$nCBPPKALgJxfTdx?2+T4TL+Li%olOGn;k*j3wJw^c>9OD42gTH$WXRNPO?U!M-JLLuu8qeWExd$mg@zHM;v8?SVB;SlmT`U36&=rhw^({Z75YTFU5d_|vfy>&;zT<<{LB)x4E<7T^JQpI??b5s3%hh=)hVxn+%`(dGaSpP!x4CQydNp|uT{1yK|%{R?w^)tA0M*Vt+WP9`p;~D=b%^cNC&kweAG~!{XW@T$osZLLnV0CAEuYYcQeW6J*?P#e|NBCjHbHzf7Q&O;DKeT^b{YceF;7QzBwHL5tC-*45S!nxgvtd8JOLpx&v1m%?2lNu-0>}sS70p8LceZsv!V!ylS-EVXNkP?G#aZ0~yKyr8dWU31!&0Jib^BnUduIP+wRT+MVTXJ~*<9%`<6ygEZ}Kzx3E5uJ3(Iix8KHAv`(~kfXUGrqAJs9<I@3_;5voWs^=E>AWldJKXi<n<b8vlyW^P)0y>DIdRIf!r(s;yG!(OdTPK;+OvQ<U>Zqro8SHNYn1GY{-_YS*7PUUcqXDhg2Z|xhmbZq$>$Q1Mh;vV!f%U;Q8s!2xG7olTWpK85tU&&^}PTMG=aTNPzp?X>WRJC<q;$Vk;df9rZN?P@2tz|_2TJ;wFe1~Ot^cmv`|5(i})ojlnwslJ4W`}%x?h)uC(<aLh%23Z2wr(uxTZCw1XHT_GSCo2fY(ax@XmDb^Np$UUu~~i8Z^D1tUW-dos(Ck#Q&Rgx%2eP{+(WG&ibyE&B%(!V<7}yUH-u++>oKl$O8*D$3g|fG3Gx}zUhi+VZ&=AIr*vPnbG=Df)j-`+=PtE(KH_GFd_~zxsYzM&X02p;|9rJ<MCn_razfQZ^)UNjp?hS=AM_8^LCp)(aOnZ6Nlf)%tz~=27xV?qI`<acR^<-1NGkPxnsi@bShHkKlw50YXPs?Sc6GaBZS7RIMO(^q{&~$<p;A(ee=Dd>PRBysQp!l&Wvc_MRy55bwL?PsY>$5{qIqQ3H@R|P<_E|O^d9;Z&L72C#dfwyUeyh`Xk)WvyJJArX4_7|FsVy8^<b@KMgL5-Z%64`t8;wSWwlB|^?kK&e$!O*8scDweR%Ex=rhw+%OT2e&j+?|Qt4c)a(&_s^drkA(Fnn6;~B7GGxb}XXnB7`k78Mpc5-k*n{jezX@_N3>wd09eavszXVGM*MO3C{D~?N2;atIP%wO71vIB}xDC<0_e?;wSrDiLHe|YgJrA}t?0pb<(IQ$9d0oi23VX$LI)hoYrMXh*;WmnTo!cONlwQVNpT&r?J)m61gLG^sKZ$Q&>vtV2GTeEUl%}CE2^=7SPc*qCz70pWbC*5}C9=1tT^?J2#LF5_o3DPF_4&6-s1&m}Q^Kpe}UwK%md_}HsWp-<Vaa3+~p?gTzc)3GY)o=b`%|f|ZXrOT|q*7AHTHQ#}L*_}P1)xbN%{sMNTJct+aV@T9c-JqvXn5^C<O1>%<q6IQ#X{YEjAc;M0j6|gt7M^jOYch6NX;*`OCa@nwQhgYLbGF7^;)xYX3cJoW=!*Os&anIROtfgTB~z@;vV!f%U01j!Aj!^uwza2T(fd#`UTDp#UR}m-D>+8s(Lujcam;(U|5fOS%_|VN^O;Qes^_;eNFLZrGHVvY1DYlWWPmDzHJerMO5uW-EP!hz*o6Brd}@RBej2A?Qp$q5vXx~{WiHye(@Xn9?lf<59A)jWZPk?dra>Kv2sbWWQToM$yCX7%Q&-PIrUt#a#_t@k7ZBuaH?}a%W|oBP|tV0bX3w*&jj^+wQoY?3Gx}zR`);MZ2c9CWm@xgs&Ya68R!w&9NPffK;jvUd?e{<j#6`XUZrDMu4rX!bBRlMU~{cxde>mNSx??o(r?R7rbTGDaW}kKXzNtlM9p93QKcWaLK5LLvsFdyR=aUGwrxWDA-`m2@jd(k=nC#L;t9h}!eNYkP{|psPEVy`tz=j4Qq@w`B#&n<^LDCof6GFtdsEMLy>)8Ra*uvY>1m-zQpHl`9raqXb7cAz&L724-6q{i`w6OhM$d4)bZg}q&KJcx#T@5G^&h5XB+qY>bZu*5qjX<{ab-$%m2GBxPpfl${du{6Ny2l?bN5KGLqef(5xPZA^+@MJ+F8s<r8&M{H2)}%Q&Q`EqHz(hab)E^gJN*^7v%!Z4DuEH75_-pXQpIO?;o*fQMq2Lb5X@h)pXN1sd+NbaJ_U@(n61YPw8l(No>V*rDsgfZ@q3z*>2+s^KhzjLi`En0oiQZG239`35<PO>29G&ZSo)F4#gb90Kr)4BcO63<#v)%Yj;GwXk&tAV_<BRNnl`UwQqU*ZogGf!d1#|(N?X0M7DQ3qeW=*RKZ-vWy)Wp6Q^Dh`826bPS<+1cRQ(ZLgOK&d~C}R@&x1+@-zAg*;dJ0pmSEm2C+_8rFgY(ZNpsCUdlL+e=g~6p-5B3M5Sa;&u+bMa@k0ua7yKNy+}&MNc|SicD;3I<q6IQ#Y)93=VtW}res>rXuWQ8?jzzE!#3Ig=U(*%zHT1lVU&1scVfGAMVxwHW_y!kd0<bob4%rNgHuPuf75UGP_bEBs!KhzLqh6Q=UUoB)I*;Yuvj?YG>=PC@noq>J-&Bn`XPgQaP1H7IN}2I8RH56P}P0DZ)(F4w`5MGUbAyc-9YbH-9DveF3)JaZcW*EqjO2+cfCn;#csW9cH?2YVpGL#`wHo3p-FD?59A)jY{N0Zc<D2sb6n+dy-0QP1^fm7FwF+dNA)APayb2csD5Q}NTPIOnr3-;XRl{&W@V~#ZR2jGO<VYR#A)40v432)Z6m0EMEz3DL)vB1U%3mcWIp#YrBYJYVzq4}qDyY=C#hp_%L(!x{2s_3^bgfZ)myl8Ox+EOVp*efs&j4IT**ek0;6##<#D}8OT}KjZ*}8fyJKy|NV{-Q{e6dIM8ibl3eRr6Z*cB2;t9h>+A-&T^%cHvVB==HVr=pw`We|S(K^de^9iAH9{XXAV0leWwQ@;=W?z1LiFtBbW4(21`fh_uN8V@HRoh;-RYkT-CbU^v;cm-R+)vA2pAN7>A?psKMO6KJwM!<xZE*1$uXJ|d5b`+s0`39mGt*wvaiMc++YzmNMW1rLbw|Qn??Bxoy=@fZX1iii#dy1OQ~i90WqQM6qHuQmVWE0h|3dW)<#)YFcJdYc75_lZH_d1DGq`g`{d$LFd-Mt88UHBF9Mw$E54LnP;$f&}WouBWPEV9zb!U5~nGAnzY!GsSa!I3fV~~}1ZG2DpQJ;r+WlAMvo_s})Vp*7ld}UgD?@f`5S95SJbd_{tx^zXBiBWT4bN@z}tz%_uBY3!CS+ZnKp08zPe0}q4kC$t8XDeQebVa;qV~CY)b$4~uUzv+#c}hHFgk(;%PFJ3ZV|iL*?^lU{ZC`#Wc#3FaqI6%5f@@!Hb@N$;t$Ss5I&*?fSF~tRg0FpLW@Y$MqnT}acs5>?bYG-nS)`k5d1z_XN12g*a&Qo8f@o2wPEVebdvah;;ZcR3abIRCVv=K7j(S;wop)b$b?HHlmse|WHf)|wPqcDLiIq`nU}@(~qk(N>U_E5GdReG^MWlmkV{l^cYnPXEZEO&7f^tctbYqZ}cWr!6`B9&Tcx6f?WS)FQj$&Dug?wdNd+$w=i&t}SEOeE0W4d%jmWfewU~~UQnXO}GY$JHMVp+0ePM)u2Wqf_`Yl#+_c5-FKatm&4%1IqyXS8@>F>YbFV@NS%Wui(+3sr8XLuVIAbEai%98_PZdT#?}Td-4S8*O2nQB)UPd7D^X4N-TXd0`7kZM<!23TSn-Zb=1PeXCnr9b9L#R8%lvWxjesF->5rXLt%!YprK=7J757RAU`>TcT@y0%}{jcTyTxWtC`N7Il1;O>YcPa;{Z!3Px?Rd}Rtwak*bx1W0|RM{XQiW4T>kFj-)<M{_VtWv)YO6-H~Tc6$j}cdJEl0%BXGPe>hLU%Y-;1%6<UeQybLd5=+i6Gn2iWPKG_X{b$i6+&^Nb8Z_}dB1*S14Cw}aBnYIWvXLfE`DXOQe+imZ?;Ei31oM%VMGIHU%ysD9C=!%OKAjuWr|UJ2ugX0U~>{+cC&SF6l`g)aY7VCb)|Y_8h?DXV^sn|W35ztEox<<Qg1F?VY*{>6mW06V_XYfbH8X#15sMAV{;#PU#NF_2We%5KywRZeS>jf5qx&JSy~rjZKY^P7j1B_S5+B)d9X)D0Z?PBWpgb^VW&fVEl^>-M?)8CYr0xi3wL&feSZK@UyDy*9(G@nW_1ToVZL!;3s8N&ZB!6?a)(e*7JF!#Re2U{b&+#M7)*JNR!IPIXOVPaEPP>|XGknsWrt2l7DH};PiG2tbAw@Q24-K4es3N~Ta{O5218-FT~rNjdAL+w5JPv3ePI!LZIN+m5q@=>Vo4uveS~LQ2X1GaP*f{+Ws`nFD`Q}Ydw3B-YmQ@d4QO+YP-6x_TZeCb8C+YRYf=G4WwTUX4M%*kNpBZIa*JAS3vO+fRdx$^e4J`m1#)?VZe1ODV4H1VF<NDpNqjL~Y>ixc3vO$RNN*QuaEn@S9d2KRTYLg>R-9&Q8hK@~U}qM6daz(%3{Y~4M{WvRWR^mE3PyFEKwSh+dV*A199m<VKwvOeY?fMaFid5PN^lihXqA3w2}X03Z*T&0R-1Hj9bjLBd|?G_X0J+M30`@xRbUfEdzEx!6-sT1Y;hG^c7k478fbZ(d0GN*YJ_)fE@owjV0$iMW|Clc6nJZtV`vC_dX#*9143V#LVFxlT!Knw2XkevUtkDRaIQ*i5p;5wUTGJ9Zi`lS7kG7mYg!q7aGz>d0e)kLX=g1<W{XaIEk<RLU3V94VwY593u<$hR(AkjT$xyW9(G@VXJ!U|Y^-c;3SxPzd}k10ah6DK7Eo=9Lv|KLe1Sw)7)*JdP+b5^V1`3rD`;hkTYM{XY>-ZR5nOALdT$L^aFJ+m26$heb$l6PR)=tF0dHlic4rMwdaG7o7eaE8b#4(&WQ}lp5ma@CQe7WjdW0iib7e|&sBSU}9VQwUEf@e12B>WSGzb_37XU0wTnAfaUuzeBZFye-Zew+F7f5Smc^_O~b7i@G5ehQ|7Z?B-g?ASU78(~_Yh`&KAYXH3xqko*JOfJ!3>P{d7hrXAWrb)9903b4b7f-(NM&DZ7gB9`UjZs(b#fOgYh`&KKVNfY5m|C&Ul|s8ZFz-qGP!UyHySQ0qiY}<KPfCCs9_x^Fg&+^5FsQjGB>|m8y5h#cn_&$F0XSfg=#LNY%GOxD!F$kSA}UPOCJbdb7c_)a%Eq!XFFe`T_#t#cRW{xX(~&%dk;asVLw2>T`E@#0C`_?7jkuSWi3Hvd2I_yb7f-(Z)IO=7fEe-UjbNSb#fORYh`&KG+%RN5hQYDUl~7nZFwyPWn*;!8eeN=qkkGO9R?N$001!`OCJ~wDggix2L)wcYrk_j5iJ%32PGW}Ga2c5ZFz-o4+$TrV=NvA6a)>0dpbND69_sqItx8{Uvn35b#i4bdu4fTqgPJ|3=szjI#n0fZFygEWn*;#Z(VC;iEemaa=v4Hsby8LWpcK8QmAEeu5xOEYfq$YWrA}?zIAQATYKerwSP_XX1j4><zBO4Y3+E2cXi`*s$o*=WT9nk-*&xcW%6W)ZFl)@p;u?+X03a0-)+5qe)(IgY<Bf@y;pzbe6?{)^I*GtXXRP5VruPuhk9`1bE;ua>t>m0Y2R|aXJztahi`THY@u6Y<zlUNb>C{eeSP^}t6_8XbG=)8<#@GyPxEBEabo3OvteoNc!zg&<8-QFPwQlfYk65><zcONb>C^de0}*{t6+2WaJ^c4<$JY!PxEKHaAM_MvtViMdxv&)<9DiHPwQu)XldVZy=8CmX1{NB`D~$CVdY@0c6Hxsy?uT8UaMhq^>e*jX61ObaZB@HyK!RWUbAg&?R<xNaN~2TVod8{p=4~|b(LjxbadZoy?lN7U8`Vo^>Dpfd*yqzd{6UdyKrLVU9(_m?R$rIb>nxcU{C93i)npcYL#zwb8p{i;&AM6k9jAzbupJ)Z)9MfcU^K*k$-<=W|>83Y(}kHV`5%_cT8$Fc%M~Va!`?Zeq<bImuG%>6LOMEb#rozYjdP+My+)QV02=X7i?vJec>IZV0_g<y<2SJGwd_h2eD^is$p2{FZd_%E2m+1f_G(EOO=0ZeN+1%v36^`TVvoqoqAt)f0S}^V}H9~W|s<6b7f<(b4D9cX1!N@8gOC')
key = b'my_secure_key'
decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
exec(marshal.loads(decrypted_data))