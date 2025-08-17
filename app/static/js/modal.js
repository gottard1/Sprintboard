document.addEventListener('DOMContentLoaded', () => {
    // Elementos do Modal
    const openModalBtn = document.getElementById('open-add-task-modal-btn');
    const modalBackdrop = document.getElementById('add-task-modal-backdrop');
    const addTaskForm = document.getElementById('add-task-form');
    
    // Botões para fechar o modal
    const cancelBtn = document.getElementById('cancel-add-task-btn');
    const closeBtn = document.getElementById('close-modal-btn');

    // Função para abrir o modal
    const openModal = () => {
        const creationDateField = document.getElementById('creation_date');
        // Formato compatível com SQL: YYYY-MM-DD HH:mm:ss
        const now = new Date();
        const timezoneOffset = now.getTimezoneOffset() * 60000;
        const localISOTime = new Date(now - timezoneOffset).toISOString().slice(0, 19).replace('T', ' ');
        creationDateField.value = localISOTime;
        
        modalBackdrop.classList.remove('hidden');
    };

    // Função para fechar o modal
    const closeModal = () => {
        modalBackdrop.classList.add('hidden');
        addTaskForm.reset();
    };

    // Event Listeners
    openModalBtn.addEventListener('click', openModal);
    cancelBtn.addEventListener('click', closeModal);
    closeBtn.addEventListener('click', closeModal);
    modalBackdrop.addEventListener('click', (event) => {
        if (event.target === modalBackdrop) {
            closeModal();
        }
    });

    // Lógica de envio do formulário
    addTaskForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(addTaskForm);
        const taskData = Object.fromEntries(formData.entries());

        if (!taskData.due_date) {
            taskData.due_date = null;
        }

        fetch('/add_task', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(taskData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                closeModal();
                window.location.reload();
            } else {
                alert('Erro: ' + (data.error || 'Não foi possível adicionar a tarefa.'));
            }
        })
        .catch(error => {
            console.error('Erro no fetch:', error);
            alert('Ocorreu um erro de comunicação. Tente novamente.');
        });
    });
});