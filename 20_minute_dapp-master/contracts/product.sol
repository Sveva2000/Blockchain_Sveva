// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TracciabilitaTessile {
    /*struct posizione {
        uint lat_nord;
        uint lat_sud;
        uint long_est;
        uint long_ovest;
    }*/

    // Struttura per memorizzare le informazioni relative a un prodotto all'inizio della filiera
    struct informazioniProdottoIniziale {
        //string GPS;
        uint[3] percentuali;
        string[3] materiali;
        string brand;
        uint timestamp;
        //qui abbiamo dimenticato il codice seriale?
    }

    // Struttura per memorizzare le informazioni relative a un prodotto alla fine della filiera
    struct informazioniProdottoFinale {
        //string GPS;
        uint[3] percentuali;
        string[3] materiali;
        string brand;
        uint timestamp;
        //qui abbiamo dimenticato il codice seriale?
    }

    mapping(uint => informazioniProdottoIniziale) idProdottoIniziale;
    mapping(uint => informazioniProdottoFinale) idProdottoFinale;
    mapping(uint => uint[3]) derivazioneProdottoFinale;

    /*
    *@param: 
    *   - uint: Percentuale di composizione del materiale 1, inserire 0 se assente
    *   - uint: Percentuale di composizione del materiale 2, inserire 0 se assente
    *   - uint: Percentuale di composizione del materiale 3, inserire 0 se assente
    *   - string: Descrizione del materiale 1, inserire "" se assente
    *   - string: Descrizione del materiale 2, inserire "" se assente
    *   - string: Descrizione del materiale 3, inserire "" se assente
    *   - string: Brand produttore del prodotto iniziale
    *   - uint: Codice seriale del prodotto iniziale
    *@dev:
    *Funzione utilizzata per salvare in blockchain i dati relativi a un prodotto che si trova all'inizio della filiera.
    *Restituisce un errore se la somma delle percentuali è inferiore a 100
    */
    function caricaProdottoIniziale(
        uint _percentuale1,
        uint _percentuale2,
        uint _percentuale3,
        string memory _materiale1,
        string memory _materiale2,
        string memory _materiale3,
        string memory _brand,
        uint _codiceSeriale
        ) public returns(string memory) {
            
            if(_percentuale1+_percentuale2+_percentuale3 != 100){
                return "Errore: la somma delle percentuali non fa 100!";
            } else {

            idProdottoIniziale[_codiceSeriale] = informazioniProdottoIniziale({
                percentuali:[_percentuale1,_percentuale2,_percentuale3],
                materiali:[_materiale1,_materiale2,_materiale3],
                brand: _brand,
                timestamp: block.timestamp
                });
            return "Caricamento effettuato";
            }
    }

    /*
    *@param: 
    *   - uint: codice seriale del prodotto 1 dal quale deriva questo prodotto finale, inserire 0 se assente
    *   - uint: codice seriale del prodotto 2 dal quale deriva questo prodotto finale, inserire 0 se assente
    *   - uint: codice seriale del prodotto 3 dal quale deriva questo prodotto finale, inserire 0 se assente
    *   - uint: Percentuale di composizione del materiale di derivazione 1, inserire 0 se assente
    *   - uint: Percentuale di composizione del materiale di derivazione 2, inserire 0 se assente
    *   - uint: Percentuale di composizione del materiale di derivazione 3, inserire 0 se assente
    *   - string: Descrizione del materiale di derivazione 1, inserire "" se assente
    *   - string: Descrizione del materiale 2 di derivazione, inserire "" se assente
    *   - string: Descrizione del materiale 3 di derivazione, inserire "" se assente
    *   - string: Brand produttore del prodotto finale
    *   - uint: Codice seriale del prodotto finale
    *@dev:
    *Funzione utilizzata per salvare in blockchain i dati relativi a un prodotto che si trova alla fine della filiera
    *e collegarlo ai prodotti dai quali deriva.
    *Restituisce un errore se la somma delle percentuali è inferiore a 100
    */
    function generaProdottoFinale(
        uint _idProdottoIniziale1,
        uint _idProdottoIniziale2,
        uint _idProdottoIniziale3,
        uint _percentuale1,
        uint _percentuale2,
        uint _percentuale3,
        string memory _materiale1,
        string memory _materiale2,
        string memory _materiale3,
        string memory _brand,
        uint _codiceSeriale
    ) public returns(string memory) {

            if(_percentuale1+_percentuale2+_percentuale3 != 100){
                return "Errore: la somma delle percentuali non fa 100!";
            } else {

            idProdottoFinale[_codiceSeriale] = informazioniProdottoFinale({
                percentuali:[_percentuale1,_percentuale2,_percentuale3],
                materiali:[_materiale1,_materiale2,_materiale3],
                brand: _brand,
                timestamp: block.timestamp
                });
            }

            derivazioneProdottoFinale[_codiceSeriale] = [
                _idProdottoIniziale1,
                _idProdottoIniziale2,
                _idProdottoIniziale3
            ];

            return "Caricamento effettuato";

    }

    /*
    *@param:
    *   -uint: codice seriale del prodotto iniziale che si vuole trovare
    *@dev:
    *Restituisce i dati del prodotto iniziale che si sta cercando
    */
    function trovaProdottoIniziale(uint _id) public view returns(
        uint[3] memory,
        string[3] memory,
        string memory,
        uint) {
            return (
            idProdottoIniziale[_id].percentuali,
            idProdottoIniziale[_id].materiali,
            idProdottoIniziale[_id].brand,
            idProdottoIniziale[_id].timestamp);
    }

    /*
    *@param:
    *   -uint: codice seriale del prodotto finale che si vuole trovare
    *@dev:
    *Restituisce i dati del prodotto finale che si sta cercando e i codici seriali dei prodotti dai quali deriva
    */
    function trovaProdottoFinale(uint _id) public view returns(
        uint[3] memory,
        string[3] memory,
        string memory,
        uint,
        uint[3] memory) {
            return (
            idProdottoFinale[_id].percentuali,
            idProdottoFinale[_id].materiali,
            idProdottoFinale[_id].brand,
            idProdottoFinale[_id].timestamp,
            derivazioneProdottoFinale[_id]);
    }
 
        
}