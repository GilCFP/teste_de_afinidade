function formatString(str) {
    // Transforma toda a string em letras minúsculas
    str = str.toLowerCase();

    // Separa a string em um array de palavras
    let words = str.split(' ');

    // Percorre todas as palavras e as capitaliza
    for (let i = 0; i < words.length; i++) {
        let word = words[i];

        // Capitaliza a primeira letra da primeira palavra
        if (i === 1) {
            word = word.charAt(0).toUpperCase() + word.slice(1);
        }
        // Verifica se a palavra contém um ponto final, exclamação ou interrogação
        else if (word.includes('.') || word.includes('!') || word.includes('?')) {
            // Capitaliza a próxima letra após o ponto final, exclamação ou interrogação
            let index = word.indexOf('.') !== -1 ? word.indexOf('.') : word.indexOf('!') !== -1 ? word.indexOf('!') : word.indexOf('?');
            word = word.substring(0, index + 1) + word.charAt(index + 1).toUpperCase() + word.slice(index + 2);
        }

        // Salva a palavra capitalizada no array
        words[i] = word;
    }

    // Junta as palavras do array em uma string e retorna
    return words.join(' ');
}


var random = [] //inicializando uma lista com indices
var counter = {} //manter traço do indice de cada inteiração
for (let j = 0; j < names.length; j++) {
    counter[names[j]] = 0
    for (let i = 0; i < quest[names[j]].length; i++) {
        random.push(names[j]) //preenche o random com o nome dos cursos, com o numero exato de materias de cada curso
    }
}
random.sort(function () {//embaralha a ordem
    return Math.random() - 0.5;
});
for (i in random) {//gera as perguntas e inputs pra cada matéria
    const text = (quest[random[i]][counter[random[i]]])
    const h4 = document.createElement("h4");
    const para = document.createElement("p");
    h4.textContent = text.split(":")[0] + ":".toUpperCase();
    para.textContent = formatString(text.split(":")[1]);
    var div = {
        "Resposta": document.createElement("div"),
        "Pergunta": document.createElement("div")
    }
    for (element in div) {
        element.className = "flex"
    }
    var p1 = document.createElement("p");
    var p1Text = document.createTextNode("Pouca afinidade");
    p1.appendChild(p1Text);
    var input = document.createElement("input")
    input.type = "range"
    input.min = "0"
    input.max = "5"
    input.name = random[i] //define a classe de cada input como o nome do curso
    var p2 = document.createElement("p");
    var p2Text = document.createTextNode("Muita afinidade");
    p2.appendChild(p2Text);
    p1.className = "pouca"
    p2.className = "muita"
    div["Resposta"].className = "resposta"
    div["Pergunta"].className = "pergunta"
    //incluindo todos os elementos nas divs
    div["Resposta"].appendChild(p1);
    div["Resposta"].appendChild(input);
    div["Resposta"].appendChild(p2);
    div["Pergunta"].appendChild(h4)
    div["Pergunta"].appendChild(para)
    //incluindo todas as divs no form
    document.querySelector("form").appendChild(div["Pergunta"])
    document.querySelector("form").appendChild(div["Resposta"])
    counter[random[i]]++
}
let submit = document.createElement("input")
submit.type = "submit"
document.querySelector("form").appendChild(submit)
