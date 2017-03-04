%Multiplica o ganho do filtro
function Fnovo = multiplicaGanho(F,G)
    Fnovo = F;
    Fnovo(1) = F(1)*G;
end