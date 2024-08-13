const apiBaseUrl = 'http://localhost:8000'; // Replace with your API URL

let apiToken = '';

function saveApiToken() {
    apiToken = document.getElementById('apiToken').value;
    if (apiToken) {
        document.getElementById('apiTokenSection').classList.add('hidden'); // Hide the section
        alert('API Token saved!');
    }
}

async function getConfigs() {
    if (!apiToken) {
        alert('Please enter and save your API token.');
        return;
    }
    try {
        const response = await fetch(`${apiBaseUrl}/get_configs/`, {
            headers: {
                'access_token': apiToken // Use the specified header name
            }
        });
        const data = await response.json();
        displayConfigs(data);
    } catch (error) {
        console.error('Error fetching configs:', error);
        document.getElementById('getConfigsResult').textContent = 'Error fetching configs';
    }
}

function displayConfigs(data) {
    let html = '<table><thead><tr><th>Resource ID</th><th>Name</th><th>URL</th><th>Destination</th></tr></thead><tbody>';
    data.forEach(config => {
        html += `<tr><td>${config.resource_id}</td><td>${config.name}</td><td>${config.url}</td><td>${config.destination}</td></tr>`;
    });
    html += '</tbody></table>';
    document.getElementById('getConfigsResult').innerHTML = html;
}

document.getElementById('addConfigForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!apiToken) {
        alert('Please enter and save your API token.');
        return;
    }
    const name = document.getElementById('name').value;
    const url = document.getElementById('url').value;
    const destination = document.getElementById('destination').value;
    try {
        const response = await fetch(`${apiBaseUrl}/add_new_config/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'access_token': apiToken // Use the specified header name
            },
            body: JSON.stringify({ name, url, destination }),
        });
        const data = await response.json();
        document.getElementById('addConfigResult').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error adding config:', error);
        document.getElementById('addConfigResult').textContent = 'Error adding config';
    }
});

async function deleteConfig() {
    if (!apiToken) {
        alert('Please enter and save your API token.');
        return;
    }
    const resourceId = document.getElementById('resourceId').value;
    try {
        const response = await fetch(`${apiBaseUrl}/rm_config/${resourceId}`, {
            method: 'DELETE',
            headers: {
                'access_token': apiToken // Use the specified header name
            }
        });
        const data = await response.json();
        document.getElementById('deleteConfigResult').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error deleting config:', error);
        document.getElementById('deleteConfigResult').textContent = 'Error deleting config';
    }
}
