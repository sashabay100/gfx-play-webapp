let tg = window.Telegram.WebApp;

// Initialize Telegram WebApp
tg.expand();
tg.setHeaderColor('secondary_bg_color');

// User data
let userData = {
    balance: 0,
    items: [],
    nextSpinTime: null
};

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
    updateUI();
});

function initializeApp() {
    // Get user data from backend
    userData.balance = 100; // Example initial balance
    updateBalance();
    updateSpinTimer();
}

function setupEventListeners() {
    // Inventory
    document.querySelector('.inventory').addEventListener('click', () => {
        showInventory();
    });

    // Roulette
    document.querySelector('.roulette').addEventListener('click', () => {
        showRoulette();
    });

    // Minecraft
    document.querySelector('.minecraft').addEventListener('click', () => {
        showMinecraft();
    });

    // Giveaways
    document.querySelector('.giveaways').addEventListener('click', () => {
        showGiveaways();
    });

    // Upgrades
    document.querySelector('.upgrades').addEventListener('click', () => {
        showUpgrades();
    });
}

function updateBalance() {
    document.getElementById('balance').textContent = userData.balance;
}

function updateSpinTimer() {
    // Update spin timer logic
    const timerElement = document.getElementById('spin-timer');
    // Example timer update
    setInterval(() => {
        const now = new Date();
        const hours = 2 - now.getHours() % 3;
        const minutes = 59 - now.getMinutes();
        const seconds = 59 - now.getSeconds();
        timerElement.textContent = `${hours}:${minutes}:${seconds}`;
    }, 1000);
}

// View functions
function showInventory() {
    tg.showPopup({
        title: 'Inventory',
        message: 'Your inventory is empty',
        buttons: [{text: 'OK'}]
    });
}

function showRoulette() {
    // Implement roulette logic
    tg.showPopup({
        title: 'Daily Spin',
        message: 'Come back later for your next spin!',
        buttons: [{text: 'OK'}]
    });
}

function showMinecraft() {
    // Implement minecraft section
    tg.showPopup({
        title: 'Minecraft',
        message: 'Coming soon!',
        buttons: [{text: 'OK'}]
    });
}

function showGiveaways() {
    // Implement giveaways section
    tg.showPopup({
        title: 'Giveaways',
        message: 'No active giveaways at the moment',
        buttons: [{text: 'OK'}]
    });
}

function showUpgrades() {
    // Implement upgrades section
    tg.showPopup({
        title: 'Upgrades',
        message: 'Upgrade system coming soon!',
        buttons: [{text: 'OK'}]
    });
}