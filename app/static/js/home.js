document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
    const columns = document.querySelectorAll(".column");

    let draggedCard = null;

    cards.forEach(card => {
        card.addEventListener("dragstart", dragStart);
        card.addEventListener("dragend", dragEnd);
    });

    columns.forEach(column => {
        column.addEventListener("dragover", dragOver);
        column.addEventListener("drop", drop);
    });

    function dragStart(e) {
        draggedCard = e.target;
        setTimeout(() => e.target.classList.add("dragging"), 0);
    }

    function dragEnd(e) {
        e.target.classList.remove("dragging");
        draggedCard = null;
    }

    function dragOver(e) {
        e.preventDefault();
        const afterElement = getDragAfterElement(this, e.clientY);
        if (afterElement == null) {
            this.appendChild(draggedCard);
        } else {
            this.insertBefore(draggedCard, afterElement);
        }
    }

    function getDragAfterElement(column, y) {
        const draggableCards = [...column.querySelectorAll('.card:not(.dragging)')];
        return draggableCards.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }

    function drop(e) {
        e.preventDefault();
        if (!draggedCard) return;

        const taskId = draggedCard.dataset.id;
        const newStatus = this.dataset.status;

        console.log(`Dropped task ${taskId} into column ${newStatus}`);
        updateTaskStatus(taskId, newStatus);
    }

    function updateTaskStatus(id, status) {
        fetch(`/update_task_status/${id}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ status: status }) // Garante que o status é enviado corretamente
        })
            .then(response => {
                if (!response.ok) {
                    // Se a resposta do servidor for um erro (4xx, 5xx), lança um erro
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json(); // Converte a resposta para JSON
            })
            .then(data => {
                if (data.success) {
                    console.log("Status da tarefa atualizado com sucesso no banco de dados.");
                    // Descomente a linha abaixo para recarregar a página e garantir 
                    // que a visualização está 100% sincronizada com o BD.
                    window.location.reload();
                } else {
                    console.error("O servidor respondeu que a atualização falhou.");
                    alert("Não foi possível atualizar a tarefa. A página será recarregada para restaurar o estado.");
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error("Erro na requisição fetch:", error);
                alert("Ocorreu um erro de comunicação com o servidor. A página será recarregada.");
                window.location.reload(); // Recarrega para evitar inconsistência visual
            });
    }
});