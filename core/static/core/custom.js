document.addEventListener('DOMContentLoaded', () => {
  // Kontextuell hjälp (tooltips)
  let tooltip;
  document.body.addEventListener('mouseenter', (e) => {
    if (e.target.classList && e.target.classList.contains('info-icon')) {
      const icon = e.target;
      const text = icon.getAttribute('data-tooltip');
      tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = text;
      document.body.appendChild(tooltip);
      const rect = icon.getBoundingClientRect();
      tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
      tooltip.style.left = rect.left + 'px';
      tooltip.classList.add('show');
    }
  }, true);

  document.body.addEventListener('mouseleave', (e) => {
    if (tooltip && e.target.classList && e.target.classList.contains('info-icon')) {
      tooltip.remove();
    }
  }, true);

  // Inline validering telefon
  const phoneField = document.getElementById('phoneField');
  if (phoneField) {
    const phoneFeedback = document.getElementById('phoneFeedback');
    phoneField.addEventListener('input', function() {
      const value = this.value;
      const phoneRegex = /^[0-9]{8,12}$/;
      if (!phoneRegex.test(value) && value.length > 0) {
        phoneFeedback.style.display = 'block';
      } else {
        phoneFeedback.style.display = 'none';
      }
    });
  }

  // Favoritmarkeringar
  document.querySelectorAll('.fav-icon').forEach(icon => {
    const fav = icon.getAttribute('data-fav') === 'true';
    if (fav) icon.classList.add('favorited');

    icon.addEventListener('click', () => {
      const nowFav = !icon.classList.contains('favorited');
      icon.classList.toggle('favorited', nowFav);
      // AJAX request kan här skickas för att spara favoritstatus
    });
  });

  // Kommandopalett
  const cmdBtn = document.querySelector('.cmd-button');
  let palette;
  if (cmdBtn) {
    palette = document.createElement('div');
    palette.className = 'cmd-palette';
    palette.innerHTML = '<input type="text" placeholder="Skriv för att navigera..."><ul><li data-url="/admin_calendar/">Gå till Kalender</li><li data-url="/admin_search/">Gå till Sök</li></ul>';
    document.body.appendChild(palette);

    cmdBtn.addEventListener('click', () => {
      palette.classList.toggle('show');
      const input = palette.querySelector('input');
      input.value = '';
      input.focus();
    });

    palette.addEventListener('click', (e) => {
      if (e.target.tagName === 'LI') {
        const url = e.target.getAttribute('data-url');
        if (url) window.location = url;
      }
    });
  }

  // Onboarding overlay
  const overlay = document.querySelector('.onboarding-overlay');
  if (overlay) {
    const doneBtn = overlay.querySelector('.done-onboarding');
    if (!localStorage.getItem('onboarding_done')) {
      overlay.classList.add('show');
    }
    doneBtn.addEventListener('click', () => {
      localStorage.setItem('onboarding_done', 'true');
      overlay.classList.remove('show');
    });
  }

  // Avancerad filterpanel - endast om advancedFilterBtn finns
  const filterBtn = document.getElementById('advancedFilterBtn');
  if (filterBtn) {
    const filterPanel = document.querySelector('.filter-panel-overlay');
    filterBtn.addEventListener('click', () => {
      filterPanel.style.display = 'block';
      filterPanel.classList.add('show');
    });
    const closeBtn = filterPanel.querySelector('.close-filter-panel');
    closeBtn.addEventListener('click', () => {
      filterPanel.classList.remove('show');
      setTimeout(() => filterPanel.style.display='none', 300);
    });
    const applyFiltersBtn = document.getElementById('applyFiltersBtn');
    applyFiltersBtn.addEventListener('click', () => {
      // Här kan du implementera logik för avancerade filter
      filterPanel.classList.remove('show');
      setTimeout(() => filterPanel.style.display='none', 300);
    });
  }

});
