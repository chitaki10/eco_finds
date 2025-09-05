fetch('http://localhost:8000/api/sample')
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById('data-list');
    data.forEach(item => {
      const li = document.createElement('li');
      li.textContent = `${item.name}`;
      list.appendChild(li);
    });
  })
  .catch(err => console.error('Error fetching data:', err));
