import React from "react";
import Image from "next/image";
import Link from "next/link";

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
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:gri-cols-4 gap-5 p-5">
      {techlist.map((tech, id: number) => {
        return (
          <div key="id" className="rounded bg-slate-300">
            <Image
              src={`http://127.0.0.1:8090/api/files/${tech.collectionId}/${tech.id}/${tech.image}`}
              width={500}
              height={500}
              alt={`logo: ${tech.name}`}
            />
            <div className="p-5">
              <h2 className="text-2xl font-bold">{tech.name}</h2>
              <Link>Get Tech Details</Link>
            </div>
          </div>
        );
      })}
    </div>
  );
}
