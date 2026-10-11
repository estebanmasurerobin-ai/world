// World : l'éditeur de Plume en application autonome, sans intelligence artificielle.
// Aucun appel à Claude ni à aucun autre service d'IA : l'éditeur fonctionne seul,
// et reste utilisable hors ligne une fois ouvert une première fois.
(() => {
  window.plumeStandalone = true;
  window.plumeNoAI = true;
  document.documentElement.classList.add('no-ai');

  if ('serviceWorker' in navigator && location.protocol === 'https:') {
    addEventListener('load', () => navigator.serviceWorker.register('sw.js', { updateViaCache: 'none' }).catch(() => {}));
  }
})();
