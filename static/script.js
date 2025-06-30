document.getElementById('loadTransactions').addEventListener('click', async () => {
    try {
        const response = await fetch('/api/transactions'); // Panggil API Flask
        const transactions = await response.json();
        const transactionsListDiv = document.getElementById('transactionsList');
        transactionsListDiv.innerHTML = ''; // Kosongkan dulu

        if (transactions.length === 0) {
            transactionsListDiv.innerHTML = '<p>Belum ada transaksi.</p>';
            return;
        }

        transactions.forEach(trans => {
            const div = document.createElement('div');
            div.className = 'transaction-item';
            div.innerHTML = `
                <strong>${trans.description}</strong> (${trans.type})<br>
                Jumlah: Rp${trans.amount.toLocaleString('id-ID')}<br>
                Kategori: ${trans.category}<br>
                Tanggal: ${trans.date}
            `;
            transactionsListDiv.appendChild(div);
        });
    } catch (error) {
        console.error('Gagal mengambil transaksi:', error);
        alert('Gagal memuat data transaksi.');
    }
});