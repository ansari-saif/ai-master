import React, { useEffect, useState } from 'react';
import TodoItem from '../components/TodoItem';
import { DefaultService, TodoRead } from '../client';

const TodoList: React.FC = () => {
  const [todos, setTodos] = useState<TodoRead[]>([]);

  useEffect(() => {
    DefaultService.listAllTodosApiV1TodosGet()
      .then(setTodos)
      .catch(console.error);
  }, []);

  const handleToggle = (id: number) => {
    const todo = todos.find((t) => t.id === id);
    if (!todo) return;

    const updatedTodo = {
      ...todo,
      is_completed: !todo.is_completed,
    };

    DefaultService.updateTodoApiV1TodosTodoIdPut({
      todoId: id,
      requestBody: updatedTodo,
    })
      .then((updated) => {
        setTodos((prev) =>
          prev.map((t) => (t.id === id ? updated : t))
        );
      })
      .catch(console.error);
  };

  const handleDelete = (id: number) => {
    DefaultService.deleteTodoApiV1TodosTodoIdDelete({ todoId: id })
      .then(() => {
        setTodos((prev) => prev.filter((t) => t.id !== id));
      })
      .catch(console.error);
  };

  return (
    <div className="todo-list">
      <h1>To-Do List</h1>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={handleToggle}
          onDelete={handleDelete}
        />
      ))}
    </div>
  );
};

export default TodoList;
