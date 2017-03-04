clear
clc

%% Declarando os valores tipicos das variaveis a serem utilizadas
%PARAMETROS PARA O FONEMA A
param = [0 1500 0 250 250 620 1660 2430 3300 3750 4900 100 6000 100 100 100 70 150 320 250 200 1000 0 0 0 0 0 0 0 0 60 0 1.2];
%PARAMETROS PARA O FONEMA E
%param = [0 1500 0 250 250 530 1680 2500 3300 3750 4900 100 6000 100 100 100 60 90 200 250 200 1000 0 0 0 0 0 0 0 0 60 0 .8];
%PARAMETROS PARA O FONEMA N
%param = [0 1500 0 270 450 480 2000 2900 3300 3750 4900 100 6000 100 100 100 40 300 300 250 200 1000 0 0 0 0 0 0 0 0 40 50 1];

%chave para escolha de configuracao do sintetizador
sw = true;
%sw = true indica a configuracao cascata
%sw = false indica a configuracao em paralelo

AV = param(30);
AF = param(29);
AH = param(28);
F0 = 130;
Ta = 1/10000; %Fa = 10kHz
t_sintese = 2; %tempo da simulacao, dado em [s]
NWS = 50;
G0 = 47;
NFC = 5;

AN = 1;
AB = param(27);

F1 = param(6);
F2 = param(7);
F3 = param(8);
F4 = param(9);
F5 = param(10);
F6 = param(11);

A1 = 0;
A2 = param(22);
A3 = param(23);
A4 = param(24);
A5 = param(25);
A6 = param(26);

B1 = param(16);
B2 = param(17);
B3 = param(18);
B4 = param(19);
B5 = param(20);
B6 = param(21);

FGP = param(1);
BGP = param(12);

FGZ = param(2);
BGZ = param(13);

FNP = param(4);
BNP = param(15);

FNZ = param(5);
BNZ = param(16);

AVS = param(31);
BGS = param(14);
FGS = param(3);

%% PARAMETROS OBTIDOS PARA A VOGAL A DA DISSERTACAO DE MESTRADO
AV = 50;
AF = 0;
AH = 50;
F0 = 120;
NWS = 100;
G0 = 55;
NFC = 5;

AN = 0;
AB = param(27);

F1 = 650;
F2 = 1450;
F3 = 2600;
F4 = 3700;
F5 = 5600;
F6 = param(11);

A1 = 0;
A2 = 0;
A3 = 0;
A4 = 0;
A5 = 0;
A6 = 0;

B1 = 110;
B2 = 130;
B3 = 130;
B4 = 200;
B5 = 300;
B6 = 300;

FGP = 0;
BGP = 100;

FGZ = 1500;
BGZ = 6000;

FNP = 270;
BNP = 100;

FNZ = 270;
BNZ = 100;

AVS = 40;
BGS = 200;
FGS = param(3);

%% COMECO DO SINTETIZADOR
%montando a sequencia de pulsos
pulsoF0 = montaSequenciaPulsos(F0, Ta, t_sintese);

%%Declarando os filtros:
[Argp, Brgp, Crgp] = calculaCoefsResonator(FGP, Ta, BGP);
RGP = [Argp, Brgp, Crgp];
[Argz, Brgz, Crgz] = calculaCoefsResonator(FGZ, Ta, BGZ);
RGZ = [Argz, Brgz, Crgz];
%[Args, Brgs, Crgs] = calculaCoefsRGS(AVS, Ta, BGS);
[Args, Brgs, Crgs] = calculaCoefsResonator(FGS, Ta, BGS);
RGS = [Args, Brgs, Crgs];

[Arnp, Brnp, Crnp] = calculaCoefsResonator(FNP, Ta, BNP);
RNP = [Arnp, Brnp, Crnp];
[Arnz, Brnz, Crnz] = calculaCoefsResonator(FNZ, Ta, BNZ);
RNZ = [Arnz, Brnz, Crnz];

[Af1, Bf1, Cf1] = calculaCoefsResonator(F1, Ta, B1);
R1 = [Af1, Bf1, Cf1];
[Af2, Bf2, Cf2] = calculaCoefsResonator(F2, Ta, B2);
R2 = [Af2, Bf2, Cf2];
[Af3, Bf3, Cf3] = calculaCoefsResonator(F3, Ta, B3);
R3 = [Af3, Bf3, Cf3];
[Af4, Bf4, Cf4] = calculaCoefsResonator(F4, Ta, B4);
R4 = [Af4, Bf4, Cf4];
[Af5, Bf5, Cf5] = calculaCoefsResonator(F5, Ta, B5);
R5 = [Af5, Bf5, Cf5];

%%Filtrando trem de pulsos F0
y1 = filtra(RGP, pulsoF0);
    
y21 = filtra(RGZ, y1);
y21 = ganhoExterno(y21, AV);
y22 = filtra (RGS, y1);
y22 = ganhoExterno(y22, AVS);
    
y2 = y21+y22;
M = max(y2);
y2 = y2/M;

if sw %%CONFIGURACAO CASCATA
    
    %Adicionando a fonte de ruido
    noise = criaRuido(Ta, t_sintese, AH);
    y2 = y2 + 0.5*noise;
    
    sound(noise,1/Ta);
    
    y31 = filtra(RNP, y2);
    y3 = filtra(RNZ, y31);
    
    y41 = filtra(R1, y3);
    y42 = filtra(R2, y41);
    y43 = filtra(R3, y42);
    y44 = filtra(R4, y43);
    y4 = filtra(R5, y44);
    
    %Caracteristica de radiacao
    y = filter([1 -1], [1], y4);
    M = max(y);
    y = y/M;
    
    %tocando o som obtido
    sound(y, 1/Ta);

else %%CONFIGURACAO PARALELO

    %gerando os ruidos
    noiseAF = 5*criaRuido(Ta, t_sintese, AF);
    
    yp1 = filtra(R1, y2);
    
    %filtro FIRST DIFFERENCE
    y2_first_difference = filter([1 -1], [1], y2);
    %y2_first_difference = y2;
    
    %adcionando a fonte de ruido
    y2_first_difference = y2_first_difference + noiseAF;
    
    ypRNP = filtra(RNP, y2_first_difference);
    yp2 = filtra(R2, y2_first_difference);
    yp3 = filtra(R3, y2_first_difference);
    yp4 = filtra(R4, y2_first_difference);
    
    yp5 = filtra(R5, noiseAF);
    %yp6 = filtra(R6, noiseAF);
    ypAB = ganhoExterno(noiseAF, AB);
    
    sum = yp1+yp2+yp3+yp4+yp5 + ypRNP + ypAB;
    
    %Radiation characteristic
    y = filter([1 -1], [1], sum);
    
    M = max(y);
    y = y/M;
    sound(y, 1/Ta);
end