import {info} from './env.js';
const body = document.querySelector('body');
const button = document.querySelector('button');
const word =  document.createElement('h1');
const para = document.createElement('para');
const randomWord = () =>{
fetch('https://random-word-api.herokuapp.com//word?number=1')
      .then(response => {
          return response.json();
      })
      .then(response =>{
        word.textContent = response;
        body.appendChild(word);
        randomDefinition(word);
      })
      .catch(err =>{
          console.log(err);
      })
}

const randomDefinition = (word) =>{
    
    fetch(`https://www.dictionaryapi.com/api/v3/references/collegiate/json/${word.textContent}?key=${info.key}`)
         .then(response =>{
             return response.json();
         })
         .then(response =>{
             console.log(response[0].shortdef[0]);
             if(response[0].shortdef !== null){
             para.textContent = "Definition: " +response[0].shortdef;
             }
             else{
                para.textContent = "No definition available";
             }
             body.appendChild(para);
         })
         .catch(err =>{
             console.log(err);
         })
}



button.addEventListener('click', function(){
    randomWord();
})
