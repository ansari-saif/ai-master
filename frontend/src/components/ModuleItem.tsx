import React from "react";
import { ModuleRead } from "../client";

interface ModuleItemProps {
  module: ModuleRead;
  onDelete: (id: number) => void;
  onEdit: (id: number) => void;
}

const ModuleItem: React.FC<ModuleItemProps> = ({
  module,
  onDelete,
  onEdit,
}) => {
  return (
    <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg shadow-sm">
      <div className="flex items-center">
        <span className={`text-lg text-gray-700`}>{module.title}</span>
      </div>
      <div>
      <button
        onClick={() => onDelete(module.id)}
        className="text-red-500 hover:text-red-700 focus:outline-none transition duration-300 ease-in-out m-1 p-1"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-5 w-5"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fillRule="evenodd"
            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
            clipRule="evenodd"
          />
        </svg>
      </button>
      <button
        onClick={() => onEdit(module.id)}
        className="text-blue-500 hover:text-blue-700 focus:outline-none transition duration-300 ease-in-out m-1 p-1"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-5 w-5"
          viewBox="0 0 24 24"
          fill="currentColor"
        >
          <path d="M16.293 2.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-12 12a1 1 0 01-.464.263l-5 1a1 1 0 01-1.213-1.213l1-5a1 1 0 01.263-.464l12-12zM17 4.414L19.586 7 17 9.586 14.414 7 17 4.414zM13.586 8L5 16.586V19h2.414L16 10.414 13.586 8z" />
        </svg>
      </button>
      </div>
    </div>
  );
};

export default ModuleItem;
