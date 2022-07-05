using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class RepositoryBase<T> : IRepositoryBase<T>
        where T : class, IRegistroBancoDados
    {
        protected readonly BancoContext _context;

        public RepositoryBase(BancoContext context) =>
            _context = context;

        public virtual async Task Add(T entity)
        {
            await _context.AddAsync(entity);
            await _context.SaveChangesAsync();
        }

        protected virtual IQueryable<T> DefaultQuery =>
            _context.Set<T>();

        public virtual async Task Delete(T entity)
        {
            _context.Remove(entity);
            await _context.SaveChangesAsync();
        }

        public virtual async Task<IEnumerable<T>> GetAll() =>
            await DefaultQuery.ToListAsync();

        public virtual async Task<T> GetById(int id) =>
            await DefaultQuery.FirstOrDefaultAsync(x => x.Id == id);

        public virtual async Task Update(T entity)
        {
            _context.Update(entity);
            await _context.SaveChangesAsync();
        }
    }
}
