[F0, ttf, A2, A3, A4, A5, A6, AB, AV, AH, AF, AVS, tt, F, BW] = makespeech2('aeiou');
[a b] = impul(ttf,F0);
FF1 = [a' b'];
[t A] = inp(ttf, F0);
FF2 = [t' A'];