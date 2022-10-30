rm -f LeptonVid.o LeptonVid
cd leptonSDKEmb32PUB
make
cd ..
gcc -O2 -Wall -W -c LeptonVid.c -l palette.o -l libbmp.o -o LeptonVid.o

gcc -O2 -Wall -W -c LeptonVid.c -o LeptonVid.o
gcc -W -O1 LeptonVid.o -LleptonSDKEmb32PUB -lLEPTON_SDK -lwiringPi -o LeptonVid


gcc -W -O1 LeptonVid.o libbmp.o palette.o -LleptonSDKEmb32PUB libLEPTON_SDK.a -lwiringPi -o LeptonVid
