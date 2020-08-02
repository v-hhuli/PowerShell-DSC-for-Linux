/*
   PowerShell Desired State Configuration for Linux

   Copyright (c) Microsoft Corporation

   All rights reserved. 

   MIT License

   Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ""Software""), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
#ifndef INCLUDED_UTIL_UNIQUE_PTR_HPP
#define INCLUDED_UTIL_UNIQUE_PTR_HPP


#include "traits.hpp"

#include <algorithm>


namespace util
{


template<typename T>
struct default_delete;

template<typename T, typename D>
struct unique_ptr_move;


// unique_ptr
//------------------------------------------------------------------------------
template<typename T, typename D = default_delete<T> >
class unique_ptr
{
public:
    typedef T element_type;
    typedef D deleter_type;
    typedef typename remove_reference<T>::type* pointer;
    typedef unique_ptr_move<T, D>  move_type;

    /*ctor*/ unique_ptr ();

    explicit /*ctor*/ unique_ptr (pointer pT);

    /*ctor*/ unique_ptr (
        pointer pT,
        typename conditional<is_reference<D>::value, D, D const&>::type del);

    explicit /*ctor*/ unique_ptr (move_type const& move_ref);

    /*dtor*/ ~unique_ptr ();

    pointer get () const;
    deleter_type& get_deleter ();
    deleter_type const& get_deleter () const;

    /*bool*/ operator bool () const;

    pointer release ();
    void reset (pointer p = pointer ());

    void swap (unique_ptr& other);

    element_type& operator * () const;
    pointer operator -> () const;

    move_type move ();

private:
    /*ctor*/ unique_ptr (unique_ptr const&); // = delete
    unique_ptr& operator = (unique_ptr const&); // = delete

    pointer m_pT;
    deleter_type m_deleter;
};


// unique_ptr (array specialization)
//------------------------------------------------------------------------------
template<typename T, typename D>
class unique_ptr<T[], D>
{
public:
    typedef T element_type;
    typedef D deleter_type;
    typedef T* pointer;
    typedef unique_ptr_move<T, D>  move_type;

    /*ctor*/ unique_ptr ();
    explicit /*ctor*/ unique_ptr (pointer pT);

    /*ctor*/ unique_ptr (
        pointer pT,
        typename conditional<is_reference<D>::value, D, D const&>::type del);

    explicit /*ctor*/ unique_ptr (move_type const& move_ref);

    /*dtor*/ ~unique_ptr ();

    pointer get () const;
    deleter_type& get_deleter ();
    deleter_type const& get_deleter () const;

    /*bool*/ operator bool () const;

    pointer release ();
    void reset (pointer p = pointer ());

    void swap (unique_ptr& other);

    element_type& operator [] (size_t i) const;

    move_type move ();

private:
    /*ctor*/ unique_ptr (unique_ptr const&); // = delete
    unique_ptr& operator = (unique_ptr const&); // = delete

    pointer m_pT;
    deleter_type m_deleter;
};


// default_delete
//------------------------------------------------------------------------------
template<typename T>
struct default_delete
{
    typedef T* pointer;

    void operator () (pointer& pT)
    {
        if (0 != pT)
        {
            delete pT;
            pT = 0;
        }
    }
};


// default_delete (array specialization)
//------------------------------------------------------------------------------
template<typename T>
struct default_delete<T[]>
{
    typedef T* pointer;

    void operator () (pointer& pT)
    {
        if (0 != pT)
        {
            delete[] pT;
            pT = 0;
        }
    }
};


// unique_ptr_move
//------------------------------------------------------------------------------
template<typename T, typename D>
struct unique_ptr_move
{
public:
    /*ctor*/ unique_ptr_move (unique_ptr_move const& ref);

    /*dtor*/ ~unique_ptr_move ();

private:
    /*ctor*/ unique_ptr_move (
        typename unique_ptr<T, D>::pointer pT,
        typename conditional<is_reference<D>::value, D, D const&>::type del);

    unique_ptr_move& operator = (unique_ptr_move const&); // = delete

    typename unique_ptr<T, D>::pointer m_pT;
    typename unique_ptr<T, D>::deleter_type m_deleter;
    
    friend class unique_ptr<T, D>;
    friend class unique_ptr<T[], D>;
};


// unique_ptr_move defs
//------------------------------------------------------------------------------
template<typename T, typename D>
/*ctor*/
unique_ptr_move<T, D>::unique_ptr_move (
    unique_ptr_move const& ref)
  : m_pT (ref.m_pT)
  , m_deleter (ref.m_deleter)
{
    unique_ptr_move& r = const_cast<unique_ptr_move&>(ref);
    r.m_pT = 0;
}

template<typename T, typename D>
/*dtor*/
unique_ptr_move<T, D>::~unique_ptr_move ()
{
    m_deleter (m_pT);
}

template<typename T, typename D>
/*ctor*/
unique_ptr_move<T, D>::unique_ptr_move (
    typename unique_ptr<T, D>::pointer pT,
    typename conditional<is_reference<D>::value, D, D const&>::type del)
  : m_pT (pT)
  , m_deleter (del)
{
    // empty
}


// unique_ptr defs
//------------------------------------------------------------------------------
template<typename T, typename D>
inline /*ctor*/
unique_ptr<T, D>::unique_ptr ()
  : m_pT (0)
  , m_deleter (deleter_type ())
{
    // empty
}

template<typename T, typename D>
inline /*ctor*/
unique_ptr<T, D>::unique_ptr (
    typename unique_ptr<T, D>::pointer pT)
  : m_pT (pT)
  , m_deleter (deleter_type ())
{
    // empty
}

template<typename T, typename D>
inline /*ctor*/
unique_ptr<T, D>::unique_ptr (
    pointer pT,
    typename conditional<is_reference<D>::value, D, D const&>::type del)
  : m_pT (pT)
  , m_deleter (del)
{
    // empty
}

template<typename T, typename D>
inline /*ctor*/
unique_ptr<T, D>::unique_ptr (
    typename unique_ptr<T, D>::move_type const& move_ref)
  : m_pT (move_ref.m_pT)
  , m_deleter (move_ref.m_deleter)
{
    move_type& m_ref = const_cast<move_type&>(move_ref);
    m_ref.m_pT = 0;
}

template<typename T, typename D>
inline /*dtor*/
unique_ptr<T, D>::~unique_ptr ()
{
    m_deleter (m_pT);
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::pointer
unique_ptr<T, D>::get () const
{
    return m_pT;
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::deleter_type&
unique_ptr<T, D>::get_deleter ()
{
    return m_deleter;
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::deleter_type const&
unique_ptr<T, D>::get_deleter () const
{
    return m_deleter;
}

template<typename T, typename D>
inline /*bool*/
unique_ptr<T, D>::operator bool () const
{
    return 0 != m_pT;
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::pointer
unique_ptr<T, D>::release ()
{
    pointer pT = m_pT;
    m_pT = 0;
    return pT;
}

template<typename T, typename D>
inline void
unique_ptr<T, D>::reset (
    typename unique_ptr<T, D>::pointer p)
{
    if (p != m_pT)
    {
        m_deleter (m_pT);
        m_pT = p;
    }
}

template<typename T, typename D>
inline void
unique_ptr<T, D>::swap (
    unique_ptr<T, D>& other)
{
    std::swap (m_pT, other.m_pT);
    std::swap (m_deleter, other.m_deleter);
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::element_type&
unique_ptr<T, D>::operator * () const
{
    return *m_pT;
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::pointer
unique_ptr<T, D>::operator -> () const
{
    return m_pT;
}

template<typename T, typename D>
inline typename unique_ptr<T, D>::move_type
unique_ptr<T, D>::move ()
{
    return move_type(release (), m_deleter);
}


// unique_ptr (array specialization) defs
//------------------------------------------------------------------------------
template<typename T, typename D>
inline /*ctor*/
unique_ptr<T[], D>::unique_ptr ()
  : m_pT (0)
  , m_deleter (deleter_type ())
{
    // empty
}

template<typename T, typename D>
inline /*ctor*/
unique_ptr<T[], D>::unique_ptr (
    T* pT)
  : m_pT (pT)
  , m_deleter (deleter_type ())
{
    // empty
}

template<typename T, typename D>
inline /*ctor*/
unique_ptr<T[], D>::unique_ptr (
    T* pT,
    typename conditional<is_reference<D>::value, D, D const&>::type del)
  : m_pT (pT)
  , m_deleter (del)
{
    // empty
}

template<typename T, typename D>
inline /*ctor*/
unique_ptr<T[], D>::unique_ptr (
    unique_ptr_move<T, D> const& move_ref)
  : m_pT (move_ref.m_pT)
  , m_deleter (move_ref.m_deleter)
{
    move_type& m_ref = const_cast<move_type&>(move_ref);
    m_ref.m_pT = 0;
}

template<typename T, typename D>
inline /*dtor*/
unique_ptr<T[], D>::~unique_ptr ()
{
    m_deleter (m_pT);
}

template<typename T, typename D>
inline typename unique_ptr<T[], D>::pointer
unique_ptr<T[], D>::get () const
{
    return m_pT;
}

template<typename T, typename D>
inline typename unique_ptr<T[], D>::deleter_type&
unique_ptr<T[], D>::get_deleter ()
{
    return m_deleter;
}

template<typename T, typename D>
inline typename unique_ptr<T[], D>::deleter_type const&
unique_ptr<T[], D>::get_deleter () const
{
    return m_deleter;
}

template<typename T, typename D>
inline /*bool*/
unique_ptr<T[], D>::operator bool () const
{
    return 0 != m_pT;
}

template<typename T, typename D>
inline typename unique_ptr<T[], D>::pointer
unique_ptr<T[], D>::release ()
{
    pointer pT = m_pT;
    m_pT = 0;
    return pT;
}

template<typename T, typename D>
inline void
unique_ptr<T[], D>::reset (
    T* p)
{
    if (p != m_pT)
    {
        m_deleter (m_pT);
        m_pT = p;
    }
}

template<typename T, typename D>
inline void
unique_ptr<T[], D>::swap (
    unique_ptr<T[], D>& other)
{
    std::swap (m_pT, other.m_pT);
    std::swap (m_deleter, other.m_deleter);
}

template<typename T, typename D>
inline typename unique_ptr<T[], D>::element_type&
unique_ptr<T[], D>::operator [] (
    size_t i) const
{
    return m_pT[i];
}

template<typename T, typename D>
inline typename unique_ptr<T[], D>::move_type
unique_ptr<T[], D>::move ()
{
    return move_type(release (), m_deleter);
}


} // namespace util


namespace std
{


template<typename T, typename D>
void
swap (
    util::unique_ptr<T, D>& lhs,
    util::unique_ptr<T, D>& rhs)
{
    lhs.swap (rhs);
}


} // namespace std


template<typename T1, typename D1, typename T2, typename D2>
bool
operator == (
    util::unique_ptr<T1, D1> const& lhs,
    util::unique_ptr<T2, D2> const& rhs)
{
    return lhs.get () == rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator == (
    T1 const* lhs,
    util::unique_ptr<T2, D> const& rhs)
{
    return lhs == rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator == (
    util::unique_ptr<T1, D> const& lhs,
    T2 const* rhs)
{
    return lhs.get () == rhs;
}

template<typename T1, typename D1, typename T2, typename D2>
bool
operator != (
    util::unique_ptr<T1, D1> const& lhs,
    util::unique_ptr<T2, D2> const& rhs)
{
    return lhs.get () != rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator != (
    T1 const* lhs,
    util::unique_ptr<T2, D> const& rhs)
{
    return lhs != rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator != (
    util::unique_ptr<T1, D> const& lhs,
    T2 const* rhs)
{
    return lhs.get () != rhs;
}

template<typename T1, typename D1, typename T2, typename D2>
bool
operator < (
    util::unique_ptr<T1, D1> const& lhs,
    util::unique_ptr<T2, D2> const& rhs)
{
    return lhs.get () < rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator < (
    T1 const* lhs,
    util::unique_ptr<T2, D> const& rhs)
{
    return lhs < rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator < (
    util::unique_ptr<T1, D> const& lhs,
    T2 const* rhs)
{
    return lhs.get () < rhs;
}

template<typename T1, typename D1, typename T2, typename D2>
bool
operator > (
    util::unique_ptr<T1, D1> const& lhs,
    util::unique_ptr<T2, D2> const& rhs)
{
    return lhs.get () > rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator > (
    T1 const* lhs,
    util::unique_ptr<T2, D> const& rhs)
{
    return lhs > rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator > (
    util::unique_ptr<T1, D> const& lhs,
    T2 const* rhs)
{
    return lhs.get () > rhs;
}

template<typename T1, typename D1, typename T2, typename D2>
bool
operator <= (
    util::unique_ptr<T1, D1> const& lhs,
    util::unique_ptr<T2, D2> const& rhs)
{
    return lhs.get () <= rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator <= (
    T1 const* lhs,
    util::unique_ptr<T2, D> const& rhs)
{
    return lhs <= rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator <= (
    util::unique_ptr<T1, D> const& lhs,
    T2 const* rhs)
{
    return lhs.get () <= rhs;
}

template<typename T1, typename D1, typename T2, typename D2>
bool
operator >= (
    util::unique_ptr<T1, D1> const& lhs,
    util::unique_ptr<T2, D2> const& rhs)
{
    return lhs.get () >= rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator >= (
    T1 const* lhs,
    util::unique_ptr<T2, D> const& rhs)
{
    return lhs >= rhs.get ();
}

template<typename T1, typename T2, typename D>
bool
operator >= (
    util::unique_ptr<T1, D> const& lhs,
    T2 const* rhs)
{
    return lhs.get () >= rhs;
}


#endif // INCLUDED_UTIL_UNIQUE_PTR_HPP
