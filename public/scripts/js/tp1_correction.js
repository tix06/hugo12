
// CORRECTION EXERCICE 2, 3 et 4

// Récupération de tous les éléments
const btnRouge = document.getElementById('btnRouge');
const btnBleu = document.getElementById('btnBleu');
const btnVert = document.getElementById('btnVert');
const curseurVitesse = document.getElementById('curseurVitesse');
const champTexte = document.getElementById('champTexte');

const afficheBouton = document.getElementById('afficheBouton');
const afficheVitesse = document.getElementById('afficheVitesse');
const afficheNom = document.getElementById('afficheNom');
const afficheClics = document.getElementById('afficheClics');

// Compteur global
let compteur = 0;

// Fonction pour incrémenter le compteur
function incrementerCompteur() {
    compteur++;
    afficheClics.textContent = compteur;
}

// Gestion du bouton rouge
function clicRouge() {
    afficheBouton.textContent = 'Rouge';
    incrementerCompteur();
}
btnRouge.addEventListener('click', clicRouge);

// Gestion du bouton bleu
function clicBleu() {
    afficheBouton.textContent = 'Bleu';
    incrementerCompteur();
}
btnBleu.addEventListener('click', clicBleu);

// Gestion du bouton vert
function clicVert() {
    afficheBouton.textContent = 'Vert';
    incrementerCompteur();
}
btnVert.addEventListener('click', clicVert);

// Gestion du curseur
function majVitesse() {
    const valeur = curseurVitesse.value;
    afficheVitesse.textContent = valeur;
}
curseurVitesse.addEventListener('input', majVitesse);

// Gestion du champ texte
function majNom() {
    const nom = champTexte.value;
    afficheNom.textContent = nom;
}
champTexte.addEventListener('input', majNom);
