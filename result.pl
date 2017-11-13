#!/org/seg/tools/freeware/perl/5.18.4/1/el-6-x86_64/bin/perl
use 5.014;
use Getopt::Std;

my %options=();
getopts("hfopxm:", \%options);
if(defined $options{f}){
    print(" \n\e[32;1m  Simulation finished...  \e[0m\n");
}
elsif(defined $options{f} || defined $options{p} || defined $options{x} ){ #Finished
        if(defined $options{p}){
            print("\n\e[36;1m  QQQQQ     QQQ     QQQQQ   QQQQQ   Q   \e[0m");
            print("\n\e[36;1m  QQ  QQ   QQ QQ   QQQ     QQQ      Q   \e[0m");
            print("\n\e[36;1m  QQQQQ    QQQQQ    QQQQ    QQQQ    Q   \e[0m");
            print("\n\e[36;1m  QQ      QQ   QQ     QQQ     QQQ       \e[0m");
            print("\n\e[36;1m  QQ      QQ   QQ  QQQQQ   QQQQQ    O   \e[0m\n\n");
        }
        elsif(defined $options{x}){
            print("\n\e[31;1m  XXXXX    XXX    XXXX  XX     X   \e[0m");
            print("\n\e[31;1m  XX      XX XX    XX   XX     X   \e[0m");
            print("\n\e[31;1m  XXXXX   XXXXX    XX   XX     X   \e[0m");
            print("\n\e[31;1m  XX     XX   XX   XX   XX         \e[0m");
            print("\n\e[31;1m  XX     XX   XX  XXXX  XXXXX  O   \e[0m\n\n");
        }
}
elsif(defined $options{o}){ #TimeOut
    #print("\n\t\e[31;47;1m  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  \e[0m");
    #print("\n\t\e[31;47;1m  XX                                XX  \e[0m");
    #print("\n\t\e[31;47;1m  XX           TIME OUT             XX  \e[0m");
    #print("\n\t\e[31;47;1m  XX                                XX  \e[0m");
    #print("\n\t\e[31;47;1m  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  \e[0m\n\n");
    print("\n\e[33;1m  XXXXXX XXXX XXX   XXX XXXXX    XXXX  XX  XX XXXXXX X   \e[0m");
    print("\n\e[33;1m    XX    XX  XXXX XXXX XX      XX  XX XX  XX   XX   X   \e[0m");
    print("\n\e[33;1m    XX    XX  XX XXX xx XXXXX   XX  XX XX  XX   XX   X   \e[0m");
    print("\n\e[33;1m    XX    XX  XX  X  XX XX      XX  XX XX  XX   XX       \e[0m");
    print("\n\e[33;1m    XX   XXXX XX     XX XXXXX    XXXX   XXXX    XX   O   \e[0m\n\n");
}
else{
    print "Usage:\n";
    print "\t-h: displays this help message\n";
    print "\t-f: simulation finished in time\n";
    print "\t-o: simulation time out\n";
    print "\t-p: simulation passed!\n";
    print "\t-x: simulation failed...\n";
}
exit;

