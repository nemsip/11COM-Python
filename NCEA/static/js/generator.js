document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.button');
    const pakehaForm = document.getElementById('pakehaForm');
    const maoriForm = document.getElementById('maoriForm');
    const generatePakeha = document.getElementById('generatePakeha');
    const generateMaori = document.getElementById('generateMaori');

    const handleFormVisibility = (showPakeha) => {
        pakehaForm.style.display = showPakeha ? 'block' : 'none';
        maoriForm.style.display = showPakeha ? 'none' : 'block';
    };

    const handleInput = (event) => {
        const form = event.target.closest('form');
        const inputs = form.querySelectorAll('input[type="text"]');
        const button = form.querySelector('button[type="submit"]');
        const isAnyFilled = Array.from(inputs).some(input => input.value.trim() !== '');
        button.disabled = !isAnyFilled;
        button.classList.toggle('bg-green-700', isAnyFilled);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const form = event.target;
        const button = form.querySelector('button[type="submit"]');
        form.submit();
        form.reset();
        button.classList.add('busy');
        form.disabled = true;
    };

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            buttons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            handleFormVisibility(button.id === 'pakeha');
        });
    });

    [pakehaForm, maoriForm].forEach(form => {
        form.addEventListener('input', handleInput);
        form.addEventListener('submit', handleSubmit);
    });
});