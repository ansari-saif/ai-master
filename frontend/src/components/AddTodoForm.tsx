import React, { useState } from 'react';
import { DefaultService, TodoCreate } from '../client';

interface AddTodoFormProps {
  onAdd: (newTodo: TodoCreate) => void;
}

const AddTodoForm: React.FC<AddTodoFormProps> = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const newTodo: TodoCreate = {
      title,
      description,
    };

    DefaultService.createTodoApiV1TodosPost({ requestBody: newTodo })
      .then(onAdd)
      .catch(console.error);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button type="submit">Add Todo</button>
    </form>
  );
};

export default AddTodoForm;
