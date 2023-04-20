import React from "react";
import Image from "next/image";

type TypeProps = {
  techlist: [
    {
      collectionId: string;
      collectionName: string;
      created: string;
      detail: string;
      id: string;
      image: string;
      name: string;
      techGroupName: string;
      updated: string;
    }
  ];
  group: string;
};

export default function TechList({ techlist, group }: TypeProps) {
  return (
    <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:gri-cols-4 gap-5 p-5">
      {techlist.map((tech, id: number) => {
        return (
          <div key="id" className="rounded bg-slate-300">
            <Image
              src={`http://127.0.0.1:8090/api/files/${tech.collectionId}/${tech.id}/${tech.image}`}
              width={500}
              height={500}
              alt={`logo: ${tech.name}`}
            />
          </div>
        );
      })}
    </div>
  );
}
