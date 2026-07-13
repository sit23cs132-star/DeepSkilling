document.getElementById("courseForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const code = document.getElementById("code").value;

    // Add to list
    const li = document.createElement("li");
    li.textContent = `${name} (${code})`;
    document.getElementById("courseList").appendChild(li);

    // Clear form
    document.getElementById("courseForm").reset();
});

// Example async fetch (mock API)
async function loadCourses() {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=5");
    const data = await response.json();
    const list = document.getElementById("courseList");

    data.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `Course: ${item.title}`;
        list.appendChild(li);
    });
}

loadCourses();
