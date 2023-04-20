import React from "react";

export default function AgendaList() {
  return (
    <div className="p-4 text-slate-100">
      <h1 className="text-xl">Agenda List</h1>
      <div>
        <div>
          <div>
            <h1></h1>
            <p></p>
          </div>
          <div>
            <button
              className="bg-amber-600 rounded-md hover:bg-amber-700 hover:text-slate-200 text-slate-100 px-6 py-2"
              type="submit"
            >
              Add
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
