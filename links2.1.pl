.\" Process this file with groff -man -Tascii links.1
.TH LINKS 1 "9 grudnia 1999"
.SH NAZWA
links \- Tekstowa przegl±darka WWW w stylu Lynksa
.SH SK£ADNIA
.B links
.RI [ opcje ]
.I URL
.SH OPIS
.B links
to tekstowa przegl±darka WWW oparta na ncurses. Posiada kolorowy interfejs,
renderuje tabele, pobiera pliki w tle, posiada menu oraz prosty i zwarty kod.
.P 
W tej chwili jeszcze nie w pe³ni obs³uguje wy¶wietlanie ramek, ale to 
nied³ugo siê zmieni.
.P
.B links
rozpoznaje lokalne (file://) oraz zdalne (http:// lub ftp://) typy URL-i.
.SH KLAWISZE
Mo¿na u¿ywaæ nastêpuj±cych kombinacji klawiszy:
.TP
.B ESC
wywo³uje menu
.TP
.B ^P, ^N   
przewiñ ekran w górê, dó³
.TP
.B [, ]
przewiñ ekran w lewo, prawo
.TP
.B góra, dó³
zaznacz odno¶nik
.TP
.B ->
wybierz odno¶nik
.TP
.B <-
powrót
.TP
.B g
przejd¼ do URL-a
.TP
.B /
szukaj
.TP
.B ?
szukaj wstecz
.TP
.B n
znajd¼ nastêpne
.TP
.B N
znajd¼ poprzednie
.TP
.B =
informacje o dokumencie
.TP
.B \e
¼ród³o dokumentu
.TP
.B d
pobierz
.TP
.B ^C
wyj¶cie
.SH OPCJE
Wiêkszo¶æ opcji mo¿e by¶ ustawionych bezpo¶rednio w przegl±darce lub w pliku
konfiguracyjnym, wiêc nie musisz przejmowaæ siê zbytnio poni¿szymi:
.TP
\f3-async-dns \f2<0>/<1>\f1
Asynchroniczna obs³uga DNS w³±czona(1)/wy³±czona(0). 
.TP
\f3-max-connections \f2<maks>\f1
Maksymalna liczba jednoczesnych po³±czeñ.
(domy¶lnie: 10)
.TP
\f3-max-connections-to-host \f2<maks>\f1
Maksymalna liczba jednoczesnych po³±czeñ z jednym serwerem.
(domy¶lnie: 2)
.TP
\f3-retries \f2<próby>\f1
Liczba prób nawi±zania po³±czenia.
(domy¶lnie: 3)
.TP
\f3-receive-timeout \f2<sek>\f1
Maksymalny czas na nawi±zanie po³±czenia.
(domy¶lnie: 120)
.TP
\f3-unrestartable-receive-timeout \f2<sek>\f1
Maksymalny czas na nawi±zanie niewznawialnego po³±czenia.
(domy¶lnie: 600)
.TP
\f3-format-cache-size \f2<liczba>\f1
Liczba stron sformatowanych dokumentów w pamiêci podrêcznej.
(domy¶lnie: 5)
.TP
\f3-memory-cache-size \f2<Kbajty>\f1
Pamiêæ podrêczna w kilobajtach.
(default: 1024)
.TP
\f3-http-proxy \f2<host:port>\f1
Nazwa i numer portu serwera HTTP proxy.
(domy¶lnie: nic)
.TP
\f3-ftp-proxy \f2<host:port>\f1
Nazwa i numer portu serwera FTP proxy.
(domy¶lnie: nic)
.TP
\f3-download-dir \f2<¶cie¿ka>\f1
Domy¶lny katalog na pobierane pliki
(domy¶lnie: aktualny katalog)
.TP
\f3-assume-codepage \f2<strona kodowa>\f1
Strona kodowa u¿ywana gdy nie jest okre¶lona ¿adna inna.
(domy¶lnie: ISO 8859-1)
.TP
\f3-version\f1
Wy¶wietla numer wersji
.BR links .
.SH PLIKI
.TP
.IP "\fI~/.links2/.links.cfg\fR"
Plik konfiguracyjny tworzony automatycznie przez
.BR links .
.SH PLATFORMY
.B links
na pewno dzia³a na nastêpuj±cych systemach Linux, FreeBSD, Solaris, IRIX, 
HPUX, Digital Unix oraz OS/2. Port dla Win32 jest nadal w fazie beta-testów.
.SH B£ÊDY
Nie mo¿na ustanowiæ po³±czenia z niektórymi serwerami FTP (Novell, NT).
Po³±czenie zawiesza siê na "Wysy³am ¿±danie".
.PP
OS/2: gdy nie powiedzie siê po³±czenie zwracany jest b³±d "Niew³a¶ciwy
argument".
.PP
OS/2: gdy jest uruchomiony w trybie pe³noekranowym, myszka pozostawia cienie.
.PP
Proszê wysy³aæ informacje o wszelkich znalezionych b³êdach pod adres Mikulas
Patocka <mikulas@artax.karlin.mff.cuni.cz>
.SH LICENCJA
.B links
jest oprogramowaniem wolnodostêpnym; mo¿esz go rozprowadzaæ dalej i/lub
modyfikowaæ na warunkach Powszechnej Licencji Publicznej GNU, wydanej przez
Fundacjê Wolnodostêpnego Oprogramowania - wed³ug wersji 2-giej tej Licencji
lub której¶ z pó¼niejszych wersji.
.SH AUTOR
Autorem
.B links
jest
.B Mikulas Patocka 
.BI <mikulas@artax.karlin.mff.cuni.cz>
.P
Ta strona manuala zosta³a napisana przez Grin <grin@tolna.net>,
wielkiego zwolennika
.BR linksa ,
który u¿ywa tej przegl±darki na systemie Debian GNU/Linux.
.P 
T³umaczenia dokona³ Arkadiusz 'Jo Joro' Sochala <jojoro@poczta.onet.pl>
.SH "ZOBACZ TAK¯E"
.BR lynx (1),
.BR w3m (1)
