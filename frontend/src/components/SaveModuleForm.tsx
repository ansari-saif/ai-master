import React, { useState } from 'react';
import { ModuleRead, ModuleService } from '../client';

interface SaveModuleFormProps {
  onSave: () => void;
  editModule : ModuleRead | object;
}

const SaveModuleForm: React.FC<SaveModuleFormProps> = ({ onSave, editModule }) => {
  // fix this add title and description
  const [title, setTitle] = useState((editModule as ModuleRead)?.title || '');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    ModuleService.createModuleApiV1ModulePost({ requestBody: { title } })
      .then(() => {
        setTitle('');
        onSave();
      })
      .catch(console.error);
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4">
      <div className="flex flex-col pd-5 m-5 space-y-4">
        <label htmlFor="module-title" className="text-gray-700">Title</label>
        <input
          id="module-title"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Title"
          className="w-full px-4 py-2 text-gray-700 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        />
      </div>
      <div className="flex justify-end">
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        >
          Save
        </button>
      </div>
    </form>
  );
};

export default SaveModuleForm;
