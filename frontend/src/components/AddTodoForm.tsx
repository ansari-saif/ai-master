import React, { useState } from 'react';
import { TodoService } from '../client';

interface AddTodoFormProps {
  onAdd: () => void;
}

const AddTodoForm: React.FC<AddTodoFormProps> = ({ onAdd }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    TodoService.createTodoApiV1TodoPost({ requestBody: { title } })
      .then(() => {
        setTitle('');
        onAdd();
      })
      .catch(console.error);
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4">
      <div className="flex items-center pd-5 m-5">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a new todo..."
          className="flex-grow px-4 py-2 text-gray-700 bg-gray-100 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        />
       
      </div>
      <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded-r-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        >
          Add
        </button>
    </form>
  );
};

export default AddTodoForm;
