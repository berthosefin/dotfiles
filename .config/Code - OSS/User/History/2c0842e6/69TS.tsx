"use Client";

import { useRouter } from "next/navigation";
import React, { FormEvent, useState } from "react";

export default function Search() {
  const [search, setSearch] = useState("");
  const router = useRouter();

  const handleSearch = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setSearch("");
    router.push(`/search/${search}`);
  };
  return <div>I am Search</div>;
}
