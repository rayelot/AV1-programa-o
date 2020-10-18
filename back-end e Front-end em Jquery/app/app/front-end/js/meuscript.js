$(function() {

    function exibir_persongens (){
        $.ajax ({
            url: 'http://localhost:5000/listar_personagens',
            method: 'GET',
            dataType: 'json',
            success: listar,
            error: function() {
                alert("Erro ao ler dados, verifique o backend.")
            }
        });
        function listar (personagens) {
            $('#corpoTabelaPersonagens').empty();
            mostrar_conteudo("tabelaPersonagem");

            for (var i in personagens) {
                lin = '<tr>' + '<td>' + personagens[i].nome + '</td>' +
                '<td>' + personagens[i].vida + '</td>' +
                '<td>' + personagens[i].ataque + '</td>' +
                '<td>' + personagens[i].defesa + '</td>' +
                '<td>' + personagens[i].pacto + '</td>' + '</tr>';
                $('#corpoTabelaPersonagens').append(lin);
            }
        }
    }

    function mostrar_conteudo(identificador){
        $("#tabelaPersonagem").addClass('invisible');
        $("#conteudoDoInicio").addClass('invisible');

        $("#" + identificador).removeClass('invisible');
    }

    $(document).on("click", "#linkListarPersonagem", function() {
        exibir_persongens();
    });

    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoDoInicio")
    });

    $(document).on("click", "#btIncluirPersonagem", function(){
        nome = $("#campoNome").val();
        vida = $("#campoVida").val();
        ataque = $("#campoAtaque").val();
        defesa = $("#campoDefesa").val();
        pacto = $("#campoPacto").val();
        var dados = JSON.stringify({ nome: nome, vida: vida, ataque: ataque, defesa: defesa, pacto: pacto });
        $.ajax({
            url: 'http://localhost:5000/incluir_personagem',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: personagemIncluido,
            error: erroAoIncluir
        });
        
        function personagemIncluido (retorno) {
            if (retorno.resultado == "ok") {
                alert("Personagem incluído com sucesso!");
                $("#campoNome").val("");
                $("#campoVida").val("");
                $("#campoAtaque").val("");
                $("#campoDefesa").val("");
                $("#campoPacto").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
    $('#modalIncluirPersonagem').on('hide.bs.modal', function (e) {
        exibir_persongens();
    });
    mostrar_conteudo("conteudoDoInicio");
});