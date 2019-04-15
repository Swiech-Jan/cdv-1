let komunikat = document.getElementById('komunikat');

let wiek = prompt('Podaj swój wiek');

if (wiek >= 18) {
  //pełnoletni
  komunikat.innerHTML = 'Jesteś pełnoletni';
}{
  //dziecko
  komunikat.innerHTML = 'Jesteś dzieckiem';
}
