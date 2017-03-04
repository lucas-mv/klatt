%%Funcao para montar o trem de pulsos com frequencia F0 e taxa de
%%amostragem 1/Ta
function P = montaSequenciaPulsos(F0, Ta, t_sintese)
    %F0: [Hz]
    %Ta: [s]
    %t_sintese: [s]
    
    %Numero de amostras
    N = ceil(t_sintese/Ta);
    %numero de pulsos
    np = ceil(F0*t_sintese);
    
    %montando o vetor de pulsos
    P = zeros([N,1]);
    aux = ceil(N/np);
    for i=1:aux:N
        P(i) = 1;
    end
end