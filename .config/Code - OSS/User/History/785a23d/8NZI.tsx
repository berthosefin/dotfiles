"use client";

import React, { useEffect, useState } from "react";

interface;

const ClientOnly = ({ children }) => {
  const [hasMounted, setHasMounted] = useState(false);

  useEffect(() => {
    setHasMounted(true);
  }, []);

  if (!hasMounted) {
    return null;
  }
  return <>{children}</>;
};

export default ClientOnly;
