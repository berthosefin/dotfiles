"use client";

import React, { useEffect, useState } from "react";

const ClientOnly = () => {
  const [hasMounted, setHasMounted] = useState(false);

  useEffect(() => {
    setHasMounted(true);
  }, []);

  if (!hasMounted) return <div>ClientOnly</div>;
};

export default ClientOnly;
