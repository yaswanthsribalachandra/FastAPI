import React, { useEffect, useState } from "react";
import "./App.css";

const BASE_URL = "http://127.0.0.1:8000";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  // 🔹 Fetch tasks
  const fetchTasks = async () => {
    const res = await fetch(`${BASE_URL}/tasks`);
    const data = await res.json();
    setTasks(data);
  };

  // 🔹 Create task
  const createTask = async (e) => {
    e.preventDefault();

    if (!title.trim()) return alert("Enter a task");

    await fetch(`${BASE_URL}/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        is_completed: false,
      }),
    });

    setTitle("");
    fetchTasks();
  };

  // 🔹 Toggle complete/incomplete
  const toggleTask = async (id, currentStatus) => {
    await fetch(`${BASE_URL}/tasks/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        is_completed: !currentStatus,
      }),
    });

    fetchTasks();
  };

  // 🔹 Delete task
  const deleteTask = async (id) => {
    await fetch(`${BASE_URL}/tasks/${id}`, {
      method: "DELETE",
    });

    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="app">
      <div className="container">
        <h2 className="title">Task Manager</h2>

        {/* Form */}
        <form onSubmit={createTask} className="form">
          <input
            type="text"
            placeholder="Enter task..."
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <button type="submit" className="btn">
            Add
          </button>
        </form>

        {/* Task List */}
        <ul className="task-list">
          {tasks.map((task) => (
            <li key={task._id} className="task-item">
              
              {/* ✅ CLICK TO TOGGLE */}
              <span
                className={`task-text ${
                  task.is_completed ? "completed" : ""
                }`}
                onClick={() =>
                  toggleTask(task._id, task.is_completed)
                }
              >
                {task.title}
              </span>

              <button
                className="delete-btn"
                onClick={() => deleteTask(task._id)}
              >
                ❌
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;